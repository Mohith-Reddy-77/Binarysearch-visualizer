# Binary Search Visualizer

This project implements a Binary Search Visualizer using Flask, HTML, CSS, and JavaScript. It allows users to input an array of integers and a target value. Upon submission, the application performs a binary search on the array to find the target value, visualizing each step of the search process.

## Features

- Input an array of integers (comma-separated in ascending order) and a target value.
- Perform binary search on the array.
- Visualize each step of the binary search process.
- Display the index of the target value if found, along with the iterations and the remaining array at each step.

## Deployment

This project has been deployed on [Render] (https://binarysearch-visualizer.onrender.com/).

## Getting Started

To run this project locally, follow these steps:

1. Clone the repository:
git clone https://github.com/Mohith-Reddy-77/Binarysearch-visualizer.git

2. Navigate to the project directory:
cd binary-search-visualizer

3. Install the required dependencies. It's recommended to use a virtual environment:
pip install -r requirements.txt

4. Run the Flask application:
python app.py

5. Open your web browser and go to `http://127.0.0.1:5000/` to access the application.

## Usage

- Enter an array of integers into the input field, separated by commas in ascending order (e.g., 1, 3, 5, 7, 9).
- Enter the target value you want to search for.
- Click on the "Search" button to initiate the binary search.
- The visualization will display the steps of the binary search algorithm along with the remaining array at each iteration.
- If the target value is found, it will display the index where it was found. Otherwise, it will indicate that the element was not found.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to open an issue or submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


