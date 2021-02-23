FROM public.ecr.aws/lambda/python:3.8

COPY app.py translate.py requirements.txt ./

RUN python3.8 -m pip install -r requirements.txt -t .

RUN mkdir data
RUN curl https://s3.amazonaws.com/models.huggingface.co/bert/Helsinki-NLP/opus-mt-en-hi/config.json -o ./data/config.json
RUN curl  -L https://s3.amazonaws.com/models.huggingface.co/bert/Helsinki-NLP/opus-mt-en-hi/pytorch_model.bin ./data/pytorch_model.bin
RUN curl https://s3.amazonaws.com/models.huggingface.co/bert/Helsinki-NLP/opus-mt-en-hi/source.spm ./data/source.spm
RUN curl https://s3.amazonaws.com/models.huggingface.co/bert/Helsinki-NLP/opus-mt-en-hi/target.spm ./data/target.spm
RUN curl https://s3.amazonaws.com/models.huggingface.co/bert/Helsinki-NLP/opus-mt-en-hi/tokenizer_config.json ./data/tokenizer_config.json

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
