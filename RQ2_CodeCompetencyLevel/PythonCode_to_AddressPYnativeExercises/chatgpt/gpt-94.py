# Given dictionary
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

# Accessing the value of key 'history'
history_value = sampleDict["class"]["student"]["marks"]["history"]

# Output the value
print(history_value)
