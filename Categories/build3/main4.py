# Machine Shop Practice Q&A Structure

# Dictionary containing topics and their corresponding Q&A
machine_shop_qa = {
    "Basics (Lathe, Tools, Techniques)": {
        "Q1": "What are some common tools and techniques used in a machine shop?",
        "A1": "Basic tools include the lathe (for turning metal), hacksaws, chisels, and grinders. Techniques include cutting, welding, and fastening."
    },
    "Properties of Metals": {
        "Q2": "What is an element, and how are metals different from nonmetals?",
        "A2": "An element is made of one type of atom. Metals have luster, malleability, and conductivity, while nonmetals are brittle.",
        "Q3": "What are some key properties of metals?",
        "A3": "Luster (shiny), malleability (easily shaped), and conductivity (good conductors of heat and electricity).",
        "Q4": "What are the five categories of metals?",
        "A4": "Noble, Alkali, Alkaline Earth, Transition, Poor metals."
    },
    "Cutting Techniques": {
        "Q5": "What is the purpose of cutting in machine shop practice?",
        "A5": "Cutting separates metals into specific shapes and sizes using tools like hacksaws, grinders, and plasma cutters.",
        "Q6": "What are some common cutting methods?",
        "A6": "Turning, Grinding, Drilling, Plasma Cutting, Water Jet Cutting."
    },
    "Fastening and Assembly": {
        "Q7": "Why is fastening important in manufacturing?",
        "A7": "Fastening ensures parts are assembled in a durable and cost-effective way.",
        "Q8": "What is the difference between screws and bolts?",
        "A8": "Screws form their own threads, while bolts are used with nuts."
    },
    "Finishing Techniques": {
        "Q9": "What is metal finishing and why is it used?",
        "A9": "Metal finishing treats surfaces to increase durability, improve appearance, and enhance properties like conductivity.",
        "Q10": "What are some common metal finishing techniques?",
        "A10": "Metal plating, Buff Polishing, Sand-Blasting, Powder Coating."
    },
    "Machining Equipment": {
        "Q11": "What is the function of shearing machines?",
        "A11": "Shearing machines cut metal sheets into size by applying a scissor-like action.",
        "Q12": "What are the different types of shears used?",
        "A12": "Pneumatic, Hydraulic, and Manual Shears."
    },
    "Welding Techniques": {
        "Q13": "What are the main types of welding?",
        "A13": "Stick Welding (SMAW), MIG Welding, TIG Welding, Oxygen-Acetylene Welding."
    },
    "Hand Tools": {
        "Q14": "What is the function of a drill press?",
        "A14": "A drill press creates holes in hard materials using a rotating drill bit.",
        "Q15": "What is a shaper, and how is it used?",
        "A15": "A shaper cuts grooves and surfaces at angles using a chisel-like tool."
    }
}

# Function to retrieve Q&A based on topic
def get_qa(topic):
    if topic in machine_shop_qa:
        qa_set = machine_shop_qa[topic]
        for q, a in qa_set.items():
            print(f"{q}: {qa_set[q]}")
            print(f"Answer: {qa_set[a]}")
            print("-" * 50)
    else:
        print("Topic not found.")

# Example of retrieving a topic
if __name__ == "__main__":
    topic = input("Enter a topic: ")
    get_qa(topic)
