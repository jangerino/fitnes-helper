"""
Fitness Helper application.

Flask web application for calculating:
- calories
- proteins
- fats
- carbohydrates
- water intake
"""

from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_bmr(weight, height, age, gender):
    """
    Calculate basal metabolic rate.

    Args:
        weight (float): User weight.
        height (float): User height.
        age (int): User age.
        gender (str): User gender.

    Returns:
        float: BMR value.
    """

    if gender == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5

    return 10 * weight + 6.25 * height - 5 * age - 161


def calculate_result(weight, height, age, gender, goal):
    """
    Calculate calories and BJU.

    Args:
        weight (float): User weight.
        height (float): User height.
        age (int): User age.
        gender (str): User gender.
        goal (str): User goal.

    Returns:
        dict: Calculated fitness indicators.
    """

    bmr = calculate_bmr(
        weight,
        height,
        age,
        gender
    )

    calories = bmr * 1.4

    if goal == "gain":
        calories += 300

    elif goal == "lose":
        calories -= 300

    protein = weight * 2
    fat = weight * 1

    carbs = (
        calories - (protein * 4 + fat * 9)
    ) / 4

    water = round(weight * 0.035, 1)

    return {
        "calories": round(calories),
        "protein": round(protein),
        "fat": round(fat),
        "carbs": round(carbs),
        "water": water
    }


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main application page.

    Returns:
        HTML page with calculated result.
    """

    result = None

    if request.method == "POST":

        weight = float(request.form["weight"])
        height = float(request.form["height"])
        age = int(request.form["age"])
        gender = request.form["gender"]
        goal = request.form["goal"]

        result = calculate_result(
            weight,
            height,
            age,
            gender,
            goal
        )

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )