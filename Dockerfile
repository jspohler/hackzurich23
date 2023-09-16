FROM python:3.11

COPY app/*.txt /app/
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r torch.txt
RUN pip install -r requirements.txt
WORKDIR ..

RUN mkdir roberta_ner_personal_info
WORKDIR /roberta_ner_personal_info
RUN wget https://huggingface.co/xooca/roberta_ner_personal_info/resolve/main/.gitattributes
RUN wget https://huggingface.co/xooca/roberta_ner_personal_info/resolve/main/.gitignore
RUN wget https://huggingface.co/xooca/roberta_ner_personal_info/resolve/main/README.md
RUN wget https://huggingface.co/xooca/roberta_ner_personal_info/resolve/main/config.json
RUN wget https://huggingface.co/xooca/roberta_ner_personal_info/resolve/main/merges.txt
RUN wget https://huggingface.co/xooca/roberta_ner_personal_info/resolve/main/pytorch_model.bin
RUN wget https://huggingface.co/xooca/roberta_ner_personal_info/resolve/main/special_tokens_map.json
RUN wget https://huggingface.co/xooca/roberta_ner_personal_info/resolve/main/tokenizer.json
RUN wget https://huggingface.co/xooca/roberta_ner_personal_info/resolve/main/tokenizer_config.json
RUN wget https://huggingface.co/xooca/roberta_ner_personal_info/resolve/main/training_args.bin
RUN wget https://huggingface.co/xooca/roberta_ner_personal_info/resolve/main/vocab.json
WORKDIR ..

COPY app/ /app
WORKDIR /app



CMD ["python", "crawler.py"]