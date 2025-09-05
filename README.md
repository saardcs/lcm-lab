# 🔁 LCM Lab

An interactive web app for practicing the Least Common Multiple (LCM) with a series of problems, designed to complement a worksheet. Students can solve problems manually on the [worksheet](https://www.education.com/worksheet/article/lcm-easy/) and then use the app to independently check their answers.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://lcm-lab.streamlit.app)

![Screenshot 1](/media/e3418aba-c3ab-4a71-8c19-559888fa66fb.png)

---

## 📘 About

**LCM Lab** helps students practice calculating the **LCM (Least Common Multiple)** of pairs of numbers using the **listing method**. The app provides a set of problems where students can input their answers and check if they're correct.

This app is designed to be used in conjunction with a [worksheet](https://www.education.com/worksheet/article/lcm-easy/), where students will solve the LCM problems on paper first, then input their answers into the app to get immediate feedback.

---

## 🎓 Educational Use

- **Target Audience**: Mathayom 1–3 students
- **Key Concepts**: Least Common Multiple (LCM), Listing Method for LCM
- **Learning Objective**: Students will practice solving LCM problems using the listing method and validate their answers with the app.

---

## 🧠 How It Works

1. **Worksheet**: Students first solve a set of LCM problems manually on a worksheet (e.g., "What is the LCM of 3 and 5?").
2. **App Check**: Once they've solved a problem, they can input their answer into the app.
3. **Immediate Feedback**: The app checks the answer and gives feedback. If correct, they can move to the next problem. If incorrect, they can try again.
4. **Completion**: After solving all problems, students receive a score and can restart the app.

---

## 📊 Progress & Feedback

- The app tracks which problem the student is on and provides a score for correct answers.
- **Immediate feedback**: After each answer, students receive either **✅ Correct!** or **❌ Incorrect. Try again!**.
- After completing all problems, the app displays the score and offers the option to restart the exercise.

---

## 🚀 Getting Started

1. Ensure that **Python 3.9+** is installed.
2. Install the required packages:

    ```bash
    pip install streamlit qrcode
    ```

3. Save the script (e.g., `streamlit-app.py`).
4. Run the app:

    ```bash
    streamlit run streamlit-app.py
    ```

---

## 📝 Worksheet Integration
This app is designed to work with the [worksheet](https://www.education.com/worksheet/article/lcm-easy/) or another worksheet containing problems like the following:

1. What is the LCM of 3 and 5?
2. What is the LCM of 2 and 7?
3. What is the LCM of 4 and 6?
4. What is the LCM of 3 and 8?
5. What is the LCM of 5 and 7?
6. What is the LCM of 6 and 9?
7. What is the LCM of 8 and 9?
8. What is the LCM of 5 and 11?

Students should solve each problem on paper using the listing method and then enter their answers into the app for immediate feedback.

---

## ✨ Customization

You can customize the LCM Lab app to better suit your needs by following these steps:

### 1. Modify the Problem Set

You can easily change the problems the students will solve. The problems are stored in the `problems` list in the code. You can add, remove, or modify any pair of numbers.

```python
problems = [
    (3, 5),  # Example pair
    (2, 7),  # Another example pair
    # Add more pairs here...
]
```

### 2. Adjust the App’s Appearance
You can change the app's appearance to match your classroom or brand by modifying the header and title. Update the st.title() and st.markdown() lines in the streamlit-app.py file to reflect a custom title or description:

```python
st.title("🔁 LCM Lab - Custom Version")
st.markdown("This version is customized for your class!")
```

### 3. Change the QR Code URL
If you want the QR code to link to a different app (for example, if you host the app on a different platform), simply change the qr_link variable:

```python
Copy code
qr_link = "https://your-new-app-link.streamlit.app"
```

### 4. Customize Feedback Messages
Feel free to customize the feedback messages given to the students based on their answers. For instance, after they submit an answer:

```python
if user_answer == correct:
    st.success("✅ Correct answer! Well done!")
else:
    st.error("❌ Incorrect. Please check your work and try again!")
```

---

## License
MIT License – free to use for teachers and students.
