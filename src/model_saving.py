from pl_modules import BasePLModule
from transformers import AutoConfig, AutoModelForSeq2SeqLM, AutoTokenizer
import torch
import omegaconf
config = AutoConfig.from_pretrained(
    'E:/CodesRepos/MGR_Gaming/Model/rebel/model/Rebel-large',
    decoder_start_token_id = 0,
    early_stopping = False,
    no_repeat_ngram_size = 0,
)

tokenizer = AutoTokenizer.from_pretrained(
    'E:/CodesRepos/MGR_Gaming/Model/rebel/model/Rebel-large',
    use_fast=True,
    additional_special_tokens = ['<obj>', '<subj>', '<triplet>']
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    'E:/CodesRepos/MGR_Gaming/Model/rebel/model/Rebel-large',
    config=config,
)
model.resize_token_embeddings(len(tokenizer))

conf = omegaconf.OmegaConf.load('outputs/2024-04-01/20-26-19/.hydra/config.yaml')
pl_module = BasePLModule(conf, config, tokenizer, model)
model = pl_module.load_from_checkpoint(checkpoint_path = 'outputs/2024-04-01/20-26-19/experiments/self_personal/last.ckpt', config = config, tokenizer = tokenizer, model = model)

model.model.save_pretrained('../model/REBEL-self_personal')
model.tokenizer.save_pretrained('../model/REBEL-self_personal')