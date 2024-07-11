"""Self-made Interpersonal RE dataset"""

from __future__ import absolute_import, division, print_function

import json
import logging
import datasets
import math
from collections import defaultdict

_DESCRIPTION = """\
    To Be Updated
"""

_URL = ""
_URLS = {
    "train": _URL + "train.json",
    "dev": _URL + "val.json",
    "test": _URL + "test.json",
}

class PERSONALConfig(datasets.BuilderConfig):
    """BuilderConfig for PERSONAL."""

    def __init__(self, **kwargs):
        """BuilderConfig for PERSONAL.
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(PERSONALConfig, self).__init__(**kwargs)


class PERSONAL(datasets.GeneratorBasedBuilder):
    """PERSONAL"""

    BUILDER_CONFIGS = [
        PERSONALConfig(
            name="plain_text",
            version=datasets.Version("1.0.0", ""),
            description="Plain text",
        ),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "title": datasets.Value("string"),
                    "context": datasets.Value("string"),
                    "triplets": datasets.Value("string"),
                }
            ),
            # No default YET!.
            supervised_keys=None,
            homepage=None, # this to fill out
        )

    def _split_generators(self, dl_manager):
        if self.config.data_files:
            downloaded_files = {
                "train":self.config.data_files["train"],   #self.config.data_dir + "self_train.json",
                "dev":  self.config.data_files["dev"],     #self.config.data_dir + "self_val.json",
                "test": self.config.data_files["test"],    #self.config.data_dir + "self_test.json",
            }
        else:
            downloaded_files = dl_manager.download_and_extract(_URLS)

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": downloaded_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": downloaded_files["dev"]}), # tutaj to odpowiednio ustawić
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": downloaded_files["test"]}),
        ]     

    def _generate_examples(self, filepath):
        """This function returns the examples in the raw (text) triplet form."""
        logging.info("generating examples from = %s", filepath)

        with open(filepath[0], encoding='utf8') as json_file:
            f = json.load(json_file)
            orig_id : int = -1
            for id_, entry in enumerate(f['entries']):
                triplets = ''
                prev_subj = None
                id_key  = list(entry.keys())[0]
                triple_sets = entry[id_key]['originaltriplesets']['originaltripleset']
                
                # Musisz juz sam załatwić by dane były w kolejności -> ogarnij by dane się zgadzały pod tym względem -> potencjalny WIP
                for triple_l in triple_sets:
                    triple = triple_l[0]
                    if prev_subj != triple['subject']:
                        prev_subj = triple['subject']
                        triplets += f"<triplet>{prev_subj}"
                    triplets += f"<subj>{triple['object']}<obj>{triple['property']}"

                for lexi in entry[id_key]['lexicalisations']:
                    orig_id += 1
                    yield str(orig_id), {
                        "title": str(orig_id),
                        "context": lexi['lex'],
                        "id": str(orig_id),
                        "triplets": triplets,
                    }      