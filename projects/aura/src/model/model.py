from langchain_community.llms import HuggingFacePipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

class LLM:
    def __init__(self, model_name: str = "google/flan-t5-small"):
        self.model_name = model_name
        self.llm = None
    
    def load_model(self):
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        model = AutoModelForCausalLM.from_pretrained(self.model_name, device_map="auto", torch_dtype=torch.float32)
        pipe = pipeline("text-generation",model=model, tokenizer=tokenizer, max_new_tokens=256, temperature=1.0, top_p=0.95, repetition_penalty=1.15)
        self.llm = HuggingFacePipeline(pipeline=pipe)
        return self.llm

    def get_llm(self):
        if self.llm is None:
            return self.load_model()
        return self.llm