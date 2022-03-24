FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/wiki28/WikiUserBot /home/wikiuserbot/ \
    && chmod 777 /home/wikiuserbot \
    && mkdir /home/wikiuserbot/bin/

COPY ./sample_config.env ./config.env* /home/wikiuserbot/

WORKDIR /home/wikiuserbot/

CMD ["python3", "-m", "userbot"]
