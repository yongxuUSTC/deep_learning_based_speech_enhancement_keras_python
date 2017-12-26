#!/usr/bin/env python
import os
import config

feats = [fname[:-4] for fname in os.listdir(config.dev_fe_mel_fd)
         if fname.endswith('.fea')]

num_feats = len(feats)
num_train = 0.95 * num_feats # Use 95% of the feats for training
width = len(str(num_feats))
fmt = '%%0%dd,%%s,%%d' % width

with open(config.dev_cv_csv_path, 'wt') as f:
    for index, feat in enumerate(feats):
        print >> f, fmt % (index, feat, 0 if index < num_train else 1)
