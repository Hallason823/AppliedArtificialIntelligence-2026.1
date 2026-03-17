from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

class LLM:
    def __init__(self, model_name: str = "Qwen/Qwen2.5-3B-Instruct"):
        self.model_name = model_name
        self.llm = None

    def load_model(self):
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        model = AutoModelForCausalLM.from_pretrained(self.model_name, device_map="auto", dtype=torch.float32)
        pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=256)
        self.llm = HuggingFacePipeline(pipeline=pipe)
        return self.llm

    def get_llm(self):
        if self.llm is None:
            return self.load_model()
        return self.llm