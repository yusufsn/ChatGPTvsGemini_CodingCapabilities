sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# Access the value of 'history' using nested indexing
history_marks = sampleDict['class']['student']['marks']['history']

print(history_marks)  # Output: 80
