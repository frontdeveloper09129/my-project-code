VARIABLE = [
    {
        "Question": "1. What is the basic unit of life?",
        "choices": ["a) Atom", "b) Cell", "c) Tissue", "d) Organ"],
        "answer": "b"
    },
    {
        "Question": "2. Which organelle is known as the 'powerhouse of the cell'?",
        "choices": ["a) Ribosome", "b) Mitochondria", "c) Nucleus", "d) Endoplasmic Reticulum"],
        "answer": "b"
    },
    {
        "Question": "3. What process do plants use to make their own food?",
        "choices": ["a) Respiration", "b) Photosynthesis", "c) Digestion", "d) Fermentation"],
        "answer": "b"
    },
    {
        "Question": "4. Which blood cells help fight infections in the human body?",
        "choices": ["a) Red blood cells", "b) White blood cells", "c) Platelets", "d) Plasma"],
        "answer": "b"
    },
    {
        "Question": "5. Which part of the plant carries water from the roots to the leaves?",
        "choices": ["a) Phloem", "b) Xylem", "c) Stomata", "d) Chloroplast"],
        "answer": "b"
    },
    {
        "Question": "6. DNA carries instructions for making what?",
        "choices": ["a) Minerals", "b) Vitamins", "c) Proteins", "d) Carbohydrates"],
        "answer": "c"
    },
    {
        "Question": "7. Which gas do humans exhale as a waste product of respiration?",
        "choices": ["a) Oxygen", "b) Nitrogen", "c) Carbon dioxide", "d) Hydrogen"],
        "answer": "c"
    },
    {
        "Question": "8. Which of these is NOT a vertebrate?",
        "choices": ["a) Dog", "b) Snake", "c) Butterfly", "d) Bird"],
        "answer": "c"
    }
]

# Quiz program
score = 0

for q in VARIABLE:
    print(q["Question"])
    for choice in q["choices"]:
        print(choice)
    
    user_answer = input("Your answer (a/b/c/d): ").lower()
    
    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}.\n")

print(f"Your final score is {score}/{len(VARIABLE)}")
