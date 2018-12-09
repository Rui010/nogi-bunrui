let model;
tf.loadModel('./js/model/model.json').then(pretrainedModel => {
    model = pretrainedModel;
});