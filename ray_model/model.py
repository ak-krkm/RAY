import os
from unsloth import FastLanguageModel
from peft import PeftModel

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ADAPTER_PATH = os.path.join(CURRENT_DIR, "weights")
BASE_MODEL_ID = "unsloth/mistral-7b-instruct-v0.3-bnb-4bit"

_model = None
_tokenizer = None


def loadModel():
    global _model, _tokenizer
    if _model is not None:
        return _model, _tokenizer
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=BASE_MODEL_ID,
        max_seq_length=2048,
        dtype=None,
        load_in_4bit=True,
    )

    FastLanguageModel.for_inference(model)

    if os.path.exists(os.path.join(ADAPTER_PATH, "adapter_config.json")):
        model = PeftModel.from_pretrained(model, ADAPTER_PATH)
    _model = model
    _tokenizer = tokenizer
    return _model, _tokenizer


def runInference(query, fileContent=None):
    try:
        model, tokenizer = loadModel()

        fullPrompt = f"[INST] {query}\n"
        if fileContent:
            fullPrompt += f"Context:\n{fileContent}\n"
        fullPrompt += "[/INST]"

        inputs = tokenizer([fullPrompt], return_tensors="pt").to("cuda")

        outputs = model.generate(
            **inputs,
            max_new_tokens=500,
            use_cache=True,
            temperature=0.7
        )

        result = tokenizer.batch_decode(outputs)[0]

        if "[/INST]" in result:
            result = result.split("[/INST]")[-1].strip()
        result = result.replace("</s>", "")

        return result

    except Exception as e:
        return f"Error during inference: {e}"