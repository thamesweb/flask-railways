# Backend - WasteAI: Snap Sort Succeed

## Problem Statement

Waste segregation is one of the primary challenges to recycling systems in major cities in our country. In India, 62 million tons of garbage is generated annually, out of which only 12 million tons is treated because we are not able to segregate waste at the source. Proper waste segregation helps reduce general waste output, identify reusable items, and set aside items for recycling. Failing to segregate waste properly results in mixed waste in landfills, causing environmental harm.

## Project Idea

The idea is to decrease human intervention and make the waste segregation process more productive. Users can take or upload an image, and the model will predict the type of waste, ensuring it lands in the correct recycle bin.

## Demo

You can view the live demo of the WasteAI frontend [here](https://wasteai.vercel.app)

Please note that while the frontend is accessible, the backend services are currently unavailable due to issues with paid deployment. For a fully functional experience, you can run the project locally by following the setup instructions provided above.


## About the Model

### Model

- **Type**: Image Classifier
- **Techniques**: Convolutional Neural Networks (CNN), Transfer Learning (VGG16 and RESNET50)

### Dataset

- **Name**: TrashNet
- **Size**: 2500+ images
- **Classes**: Cardboard, Glass, Metal, Paper, Plastic, Trash

### Metrics

- **Accuracy**: 89.12%

## Tech Stack

- **Backend**: Flask, MongoDB
- **Deployment**: Docker & DigitalOcean

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/ssahibsingh/wasteai-backend.git
   cd wasteai-backend
   ```
2. Create a virtual environment and activate it:
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Start the Flask server:
```bash
flask run
```
5. The server will be running at http://localhost:5000.

## Future Scope
* Integration with Sensor Technologies
* Integration with Smart Waste Bins
* ML Model Optimization
* Mobile Application Development
* Real-Time Monitoring and Feedback

## Frontend Repository
For information about the frontend, please refer to the [WasteAI Frontend Repository](https://github.com/ssahibsingh/wasteai-frontend).
