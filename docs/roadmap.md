## Roadmap <img src="https://github.githubassets.com/images/icons/emoji/unicode/1f9ed.png?v8" alt="fleur_de_lis" width="18" height="18">

0. Build the basic skeleton of the kafka messaging service between the dl-backend, db-handeller and app-backend.
    1. Create a docker compose with the following services: dl-backend, db-handeller, app-backend, zookeeper and kafka.
    2. Decide the message schema for the kafka messages.
    3. Test the messaging service
1. Build the image classification pipeline, with support for LeNet and MNIST.
2. Build the object detection pipeline, with support for YoLo and Pascal-VOC.
3. Build the monitoring dashboard for training.
4. Build support for user accounts.
5. Build the inference pipeline for image classification, where the user can upload an image and use a model he/she trained previously to inference on the image.
6. Build the inference pipeline for object detection, where the user can upload an image and use a model he/she trained previously to inference on the image.
7. Build a labeller, where users can make custom datasets.
8. Extend the model and dataset zoo.
9. Deploy on cloud (to be determined)
