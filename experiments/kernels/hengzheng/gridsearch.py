def build_gridsearch_params():
    params = {}
    params['tokenizer'] = ['space', 'word_tokenize']
    params['preprocessors'] = [
        ['lower', 'punct', 'number', 'hengzheng_mispell', 'keras'],
        ['lower', 'punct', 'number', 'hengzheng_mispell'],
    ]
    params['embedding.standardize'] = [True, False]
    # params['featurizer.n_finetune'] = [1, 2]
    # params['model.embed.alpha'] = [1e-5, 1e-4]
    # params['model.mlp.bn'] = [True, False]
    # params['model.embed.position'] = [True, False]
    # params['model.embed.dropout'] = [0.1, 0.2, 0.3]
    # params['model.embed.n_hidden'] = [0, 128]
    # params['model.mlp.n_hidden'] = [64, 128]
    # params['model.mlp.n_layers'] = [2, 3]

    return params
