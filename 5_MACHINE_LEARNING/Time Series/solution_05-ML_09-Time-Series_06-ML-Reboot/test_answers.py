# Define the correct answers and explanations
correct_answers = {
    "question_1": ("C", "Feature selection focuses on reducing the dimensionality of the dataset by choosing only relevant features, while feature engineering involves creating new features from existing ones."),
    "question_2": ("B", "Using the latitude and longitude points for each listing to create a distance_from_downtown feature would be a useful example of feature engineering, as it can provide valuable information about the location of the listings."),
    "question_3": ("B", "The regular expression re.search(r'\\d+(\\.\\d+)?', text) matches any floating-point number in the text."),
    "question_4": ("B", "The primary purpose of performing a train-test split in data science is to divide the dataset into two parts: one for training the model and one for testing its performance on unseen data."),
    "question_5": ("D", "The purpose of applying Min-Max Scaler to features in data preprocessing for machine learning is to scale the features to a specific range, usually between 0 and 1."),
    "question_6": ("C", "We scale our data in machine learning to avoid numerical instability and speed up the optimization process."),
    "question_7": ("C", "The simplest and most common baseline guess for a machine learning regression model is to use the mean of the target variable as the prediction."),
    "question_8": ("A", "The coefficient of determination, R-squared, measures the percentage of variance in the dependent variable explained by the independent variable/s."),
    "question_9": ("A", "A Random Forest algorithm creates multiple decision trees and combines their predictions to make more accurate and robust predictions."),
    "question_10": ("B", "We perform cross-validation in machine learning to estimate the model's performance on unseen data and assess its generalization ability."),
    "question_11": ("A", "In binary classification, precision measures the ability of a model to correctly identify positive instances, while recall measures the ability to correctly identify negative instances."),
    "question_12": ("C", "The impact of a one-minute increase in the Arrival Delay in Minutes feature on the model's results probably has a fairly small impact given that the large coefficient is based on our MinMax scaled data."),
    "question_13": ("B", "Based on the provided DataFrame showing the coefficients of a logistic regression model, the feature Inflight Entertainment appears to have the most significant impact on the model's predictions."),
    "question_14": ("C", "In layman's terms, the K-means algorithm randomly selects K data points as cluster centers, then assigns each data point to the nearest center and recalculates the center's position based on the data points in that cluster."),
    "question_15": ("A", "Principal Component Analysis (PCA) is an example of an unsupervised learning technique used for feature reduction and data dimensionality reduction."),
}

# Define incorrect answers and explanations for each question
incorrect_explanations = {
    "question_1": {
        "A": "Feature selection does not involve creating new features from existing ones.",
        "B": "Feature selection does not involve transforming numerical features into categorical ones.",
        "D": "Feature selection is not limited to linear models; it can be used for any model type.",
    },
    "question_2": {
        "A": "Adding together bedrooms and beds would not provide meaningful information about the location of the listings.",
        "C": "Price divided by bedrooms does not capture the spatial aspect of the data.",
        "D": "Converting review_scores_rating into a categorical variable would not be useful for distance calculations.",
    },
    "question_3": {
        "A": "The regular expression matches floating-point numbers, not just sequences of digits.",
        "C": "The regular expression also matches decimal numbers, not just integers.",
        "D": "The regular expression does not require the sequence of characters to start with a digit.",
    },
    "question_4": {
        "A": "Train-test split does not involve dividing the dataset into multiple subsets for parallel processing.",
        "C": "Train-test split does not involve merging two datasets.",
        "D": "Train-test split does not affect whether the model has access to the entire dataset during training.",
    },
    "question_5": {
        "A": "Min-Max Scaler is used for scaling features, not for eliminating outliers.",
        "B": "Min-Max Scaler does not aim to reduce the dimensionality of the data.",
        "C": "Min-Max Scaler does not standardize the features to have a mean of 0 and standard deviation of 1.",
    },
    "question_6": {
        "A": "Scaling data does not directly reduce the number of features in the dataset.",
        "B": "Scaling data does not guarantee that the model always converges to the global optimum.",
        "D": "Scaling data does not eliminate outliers and anomalies from the dataset.",
    },
    "question_7": {
        "A": "The simplest and most common baseline guess for a machine learning regression model is not the median of the target variable.",
        "B": "The baseline guess is not the maximum value of the target variable.",
        "D": "The baseline guess is not the minimum value of the target variable.",
    },
    "question_8": {
        "B": "R-squared measures the percentage of variance in the dependent variable explained by the independent variable/s, not the other way around.",
        "C": "R-squared does not measure the percentage of correct predictions made by the regression model.",
        "D": "R-squared does not measure the percentage of outliers in the dataset that affect the regression model's performance.",
    },
    "question_9": {
        "B": "Random Forest does not randomly select features to build a single decision tree.",
        "C": "Random Forest does not use a random process to shuffle the data and find the best fit.",
        "D": "Random Forest does not rely on the randomness of the data without using decision trees.",
    },
    "question_10": {
        "A": "Cross-validation is used to estimate the model's performance on unseen data, not just on the training data.",
        "C": "Cross-validation does not increase the size of the training data.",
        "D": "Cross-validation is used to address overfitting but does not prevent the model from memorizing the training data.",
    },
    "question_11": {
        "B": "Precision measures the ability of a model to correctly identify negative instances, not positive ones.",
        "C": "Precision does not measure the overall accuracy of the model.",
        "D": "The provided explanation for precision is incorrect, making this option the most suitable incorrect explanation.",
    },
    "question_12": {
        "A": "The impact of a one-minute increase in Arrival Delay in Minutes cannot be directly determined from the provided coefficients given that we have scaled.",
        "B": "The impact of the feature on the model's predictions cannot be assumed to be zero.",
    },
    "question_13": {
        "A": "The absolute value of this feature is lower than that of Inflight entertainment.",
        "C": "The absolute value of this feature is lower than that of Inflight entertainment.",
        "D": "The absolute value of this feature is lower than that of Inflight entertainment.",
    },
    "question_14": {
        "A": "K-means algorithm does not find the mean of all data points to create clusters.",
        "B": "K-means algorithm does not calculate the distance between each data point and its nearest neighbor to create clusters - it uses centroids instead.",
        "D": "K-means algorithm does not sort the data points to assign them to clusters.",
    },
    "question_15": {
        "B": "Decision Tree is a supervised learning technique that requires labeled data.",
        "C": "Support Vector Machine (SVM) is a supervised learning technique that requires labeled data.",
        "D": "Random Forest is a supervised learning technique that requires labeled data.",
    },
}

# Checking and providing explanations for answers
def check_answers(student_answers):
    for question, (correct_answer, explanation) in correct_answers.items():
        student_answer = student_answers[question]

        print(f"\nQuestion {question[-2:]}:")
        print(f"Your answer: {student_answer}")
        print(f"Correct answer: {correct_answer}")

        if student_answer == correct_answer:
            print("Correct! Well done.")
        else:
            print("Incorrect. Here's why:")
            print(f"Explanation: {explanation}")
            print("Other options and why they are wrong:")
            for option, wrong_explanation in incorrect_explanations[question].items():
                if option != correct_answer:
                    print(f"Option {option}: {wrong_explanation}")

# Call the function to check the answers
