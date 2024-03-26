#!/usr/bin/env bash
curr_dir=$(pwd)

mkdir -p data

wget -r -nH --cut-dirs=100 --reject "index.html*" --no-parent http://lavis.cs.hs-rm.de/storage/spert/public/datasets/conll04/ -P ${curr_dir}/data/conll04
wget -r -nH --cut-dirs=100 --reject "index.html*" --no-parent http://lavis.cs.hs-rm.de/storage/spert/public/datasets/scierc/ -P ${curr_dir}/data/scierc
wget -r -nH --cut-dirs=100 --reject "index.html*" --no-parent http://lavis.cs.hs-rm.de/storage/spert/public/datasets/ade/ -P ${curr_dir}/data/ade