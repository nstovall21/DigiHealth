import networkx as nx

def Irregular Vaginal Bleeding():
   # flowchart for Irregular Vaginal Bleeding

   # define
   flowchart = {}
  
   flowchart['N1'] = "Could you be pregnant?"
   flowchart['N2'] = "Could you be more than three months pregnant?"
   flowchart['N3'] = "Do you have severe abdominal pain?"
   flowchart['A1'] = "See a doctor immediately. Bleeding 3 months or more into a pregnancy may be a sign of an impedning miscarriage. See also vaginal bleeding during pregnancy."
   flowchart['A2'] = "Emergency. Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest emergency department. A pregnancy may be developing outside the uterus."
   flowchart['N4'] = "Has your pregnancy been confirmed?"
   flowchart['A3'] = "See a doctor immediately. Some women have slight vaginal bleeding, or spotting, early in pregnancy. However, you may be having a miscarriage. See also vaginal bleeding during pregnancy."
   flowchart['N5'] = "Did you have your last period more than 6 months ago?"
   flowchart['A4'] = "See your doctor immediately. You could be pregnant. However, vaginal bleeding can also be a sign of cancer of the uterus or cancer of the cervix, especially if you are over age 45."
   flowchart['N6'] = "Do you have a heavy, watery vaginal discharge, or does the bleeding occur immediately after intercourse?"
   flowchart['A5'] = "See a doctor immediately. You may have cancer of the cervix or cancer of the uterus."
   flowchart['N7'] = "Do you have an intrauterine device (IUD)?"
   flowchart['N8'] = "Do you have severe abdominal pain?"
   flowchart['A6'] = "Emergency. Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest emergency department. A pregnancy may be developing outside the uterus."
   flowchart['A7'] = "See your doctor. An IUD sometimes causes vaginal bleeding."
   flowchart['N9'] = "Are you taking oral contraceptives?"
   flowchart['A8'] = "Talk to your doctor. You are probably having breakthrough bleeding, which is common in women taking oral contraceptives."
   flowchart['N10'] = "Was the bleeding like that of a period?"
   flowchart['N11'] = "Have you started your periods within the past 3 years?"
   flowchart['A9'] = "Talk to your doctor. Irregular periods are common during the first 3 years of mensturation. See irregular periods."
   flowchart['N12'] = "Are you in your 40s?"
   flowchart['A10'] = "Talk to your doctor. Irregular periods are common as women approach menopause. See also irregular periods"
   flowchart['A11'] = "See your doctor if you are unable to make a diagnosis from this chart."

   edges_with_conditions = [("N1", "N2", "Yes"),
                           ("N1", "N5", "No"),
                           ("N2", "N3", "No"),
                           ("N2", "A1", "Yes"),
                           ("N3", "A2", "Yes"),
                           ("N3", "N4", "No"),
                           ("N4", "A3", "Yes"),
                           ("N4", "N5", "No"),
                           ("N5", "N6", "No"),
                           ("N5", "A4", "Yes"),
                           ("N6", "A5", "Yes"),
                           ("N6", "N7", "No"),
                           ("N7", "N8", "Yes"),
                           ("N7", "N9", "No"),
                           ("N8", "A6", "Yes"),
                           ("N8", "A7", "No"),
                           ("N9", "A8", "Yes"),
                           ("N9", "N10", "No"),
                           ("N10", "A11", "No"),
                           ("N10", "N11", "Yes"),
                           ("N11", "A9", "Yes"),
                           ("N11", "N12", "No"),
                           ("N12", "A10", "Yes"),
                           ("N12", "A11", "No")]

   G = nx.DiGraph()
   G.add_nodes_from(flowchart.items())

   # Add edges to the graph
   for edge in edges_with_conditions:
       G.add_edge(edge[0], edge[1], condition=edge[2])
  
   # print(G.nodes(data=False))
   return flowchart, G


def Difficulty_Swallowing_Flowchart():
    # flowchart for difficulty swallowing
    
    # Define nodes (questions and advice)
    flowchart = {}
    flowchart['N1'] = "Do you have a sore throat?"
    flowchart['A1'] = "See a doctor immediately. Something may be lodged in your throat."
    flowchart['N2'] = "Could you have swallowed something (such as a fish bone)?"
    flowchart['F1'] = "Sore Throat"
    flowchart['N3'] = "Does food seem to stick high up in your chest after you swallow it?"
    flowchart['N4'] = "Do you sometimes experience pain in your chest, particularly when you squat, bend, or lie down?"
    flowchart['A2'] = "See your doctor. Your esophagus may be scarred as a result of acid reflux. See Gastroesophageal Reflux Disease."
    flowchart['N5'] = "Are you having difficulty swallowing, do you regurgitate food you swallow, and have you lost a lot of weight in a short time (more than 10 pounds in 10 weeks)?"
    flowchart['A3'] = "See a doctor immediately. You may have a disorder of the esophagus, such as achalasia or a pharyngeal pouch. You may also have a scarred esophagus from chronic acid reflux or possibly cancer of the esophagus, especially if you are over 40."
    flowchart['N6'] = "Do you swallow normally but feel a lump in your throat when you swallow or feel that the food will not go down?"
    flowchart['A4'] = "See your doctor. Your swallowing problem may be a symptom of anxiety or gastroesophageal reflux disease."
    flowchart['A5'] = "See your doctor if you are unable to make a diagnosis from this chart."
    flowchart['A6'] = "If you have persistent difficulty swallowing, see a doctor immediately. Difficulty swallowing that persists or worsens over time may be a symptom of cancer of the esophagus, especially if you are over 40."
    
    # Define edges with conditions
    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N2", "A1", "Yes"),
        ("N1", "N3", "No"),
        ("N2", "F1", "No"),
        ("N3", "N4", "Yes"),
        ("N4", "N5", "No"),
        ("N4", "A2", "Yes"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N3", "N6", "No"),
        ("N6", "A4", "Yes"),
        ("N6", "A5", "No")
    ]

    # Create the graph
    G = nx.DiGraph()
    G.add_nodes_from(flowchart.items())

    # Add edges to the graph
    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G

import networkx as nx

def Sore_Throat_Flowchart():
    # flowchart for sore throat
    
    # Define nodes (questions and advice)
    flowchart = {}
    flowchart['N1'] = "Is your temperature 100°F or higher?"
    flowchart['N2'] = "Do you have two or more of the following symptoms: headache, cough, aching joints or bones?"
    flowchart['A1'] = "Talk to your doctor. You probably have a viral infection such as influenza."
    flowchart['N3'] = "Do you have swelling or tenderness in your neck?"
    flowchart['N4'] = "Is the swollen or tender area in front of your ear or at the angle of the jaw?"
    flowchart['A2'] = "See your doctor. You may have mumps."
    flowchart['N5'] = "Do you have a stuffy or runny nose, or have you been sneezing?"
    flowchart['A3'] = "You probably have a cold."
    flowchart['A4'] = "See your doctor. You probably have strep throat, tonsillitis, or pharyngitis. If your symptoms persist for more than a week, you may have infectious mononucleosis."
    flowchart['N6'] = "Do you smoke or drink a lot of alcohol, or were you in a smoky place (such as a bar) just before your throat got sore?"
    flowchart['A5'] = "Call your doctor. Smoking, inhaling secondhand smoke, and drinking alcohol can all cause throat inflammation. See pharyngitis."
    flowchart['N7'] = "Are you hoarse, or have you lost your voice?"
    flowchart['A6'] = "See the chart *Hoarseness or Loss of Voice*."
    flowchart['A7'] = "See your doctor if you are unable to make a diagnosis from this chart and your sore throat persists for more than 2 days."
    
    # Define edges with conditions
    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N1", "N3", "No"),
        ("N3", "N4", "Yes"),
        ("N4", "A2", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "A4", "No"),
        ("N6", "A5", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "N7", "No"),
        ("N7", "A6", "Yes"),
        ("N7", "A7", "No")
    ]

    # Create the graph
    G = nx.DiGraph()
    G.add_nodes_from(flowchart.items())

    # Add edges to the graph
    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

    return flowchart, G

def Hoarseness_Loss_Of_Voice_Flowchart():
    # Flowchart for Hoarseness or Loss of Voice
    
    # Define nodes (questions and advice)
    flowchart = {}
    flowchart['N1'] = "Did the hoarseness begin within the past 3 days?"
    flowchart['N2'] = "Do you (or did you recently) have a cold, cough, or sore throat?"
    flowchart['A1'] = "You probably have inflammation of the vocal cords."
    flowchart['N3'] = "Does your job require you to talk a lot—for example, are you a teacher or a lawyer?"
    flowchart['A2'] = "See your doctor. You may have persistent inflammation of the vocal cords or a growth on a vocal cord."
    flowchart['N4'] = "Were you talking more than usual just before the hoarseness developed or before you lost your voice?"
    flowchart['A3'] = "Talking too much can cause inflammation of the vocal cords."
    flowchart['N5'] = "Have you recently been feeling tense, nervous, or anxious?"
    flowchart['A4'] = "Anxiety can cause a sudden loss of voice."
    flowchart['N6'] = "Have you been drinking a lot of alcohol?"
    flowchart['A5'] = "Excessive drinking can lead to inflammation of the vocal cords."
    flowchart['N7'] = "Do you smoke, or have you been in a smoky place (such as a bar)?"
    flowchart['A6'] = "See your doctor. Smoking can lead to inflammation of the vocal cords. However, it can also cause cancer."
    flowchart['N8'] = "Do you have two or more of the following symptoms: sensitivity to cold weather, dry skin or dry hair, unexplained weight gain, unexplained fatigue?"
    flowchart['A7'] = "See your doctor. You may have an underactive thyroid gland."
    flowchart['N9'] = "Has the hoarseness or loss of voice lasted longer than a week?"
    flowchart['N10'] = "Have you had several episodes of hoarseness or voice loss in the past 6 months?"
    flowchart['A8'] = "See a doctor immediately. You could have a polyp on a vocal cord or cancer of the larynx."
    flowchart['A9'] = "See your doctor if you are unable to make a diagnosis from this chart and your hoarseness persists for more than a week."
    flowchart['A10'] = "If you have persistent hoarseness, see a doctor immediately. Chronic hoarseness or loss of voice lasting more than a week may be a sign of cancer of the larynx."

    # Define edges with conditions
    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N2", "A1", "Yes"),
        ("N2", "N4", "No"),
        ("N1", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "N6", "No"),
        ("N4", "A3", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "A4", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A6", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "A7", "Yes"),
        ("N8", "N9", "No"),
        ("N9", "A8", "Yes"),
        ("N9", "N10", "No"),
        ("N10", "A8", "Yes"),
        ("N10", "A9", "No")
    ]

    # Additional advice for persistent hoarseness
    persistent_advice = flowchart['A10']

    return flowchart, edges_with_conditions, persistent_advice

    G = nx.DiGraph()
    G.add_nodes_from(flowchart.items())

    # Add edges to the graph
    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

def Difficulty_Breathing_Flowchart():
    # Flowchart for Difficulty Breathing
    
    # Define nodes (questions and advice)
    flowchart = {}
    flowchart['N1'] = "Did your breathing difficulty begin within the past few days?"
    flowchart['N2'] = "Do you have chest pain?"
    flowchart['N3'] = "Is the pain crushing, or does it radiate from the breastbone or upper abdomen to your jaw, neck, or arms?"
    flowchart['A1'] = "EMERGENCY! Get medical help now. Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You could be having a HEART ATTACK."
    flowchart['N4'] = "Is the pain worse when you inhale?"
    flowchart['A2'] = "EMERGENCY! Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. You may have a blood clot in a lung, a collapsed lung, or pleurisy."
    flowchart['A3'] = "See a doctor immediately. You could have PNEUMONIA or ACUTE BRONCHITIS."
    flowchart['A4'] = "EMERGENCY! Get medical help now! Call 911 or your local emergency number or have someone take you to the nearest hospital emergency department. If the pain persists after you rest for 5 minutets, you could be having a HEART ATTACK. For first aid, see HEART ATTACK. However, you could also be having an attack of angina, a symptom of HEART DISEASE."
    flowchart['N5'] = "Is your temperature 100°F or above, or are you coughing up greenish yellow or rust-colored colored phlegm?"
    flowchart['N6'] = "Have you been Wheezing?"
    flowchart['N7'] = "Do you feel light-headed, or are your hands and feet numb and tingling?"
    flowchart['N8'] = "Has your breathing become increasingly difficult in the past weeks or months?"
    flowchart['N9'] = "Do you cough up thick gray or greenish-yellow mucus most days?"
    flowhcart['F1'] - "Wheezing"
    flowchart['N10'] = "Do you work in a dusty atmosphere (such as a mine or quarry)?"
    flowchart['A5'] = "You could have a lung disease caused by long-term exposure to dust. See OCCUPATIONAL LUNG DISEASES (p. 645)."
    flowchart['A6'] = "See your doctor. You probably have a lung disease such as CHRONIC BRONCHITIS, EMPHYSEMA, or PNEUMONIA."
    flowchart['N11'] = "Do your ankles look unusually puffy, or does pressing on them with your fingers leave an indentation?"
    flowchart['A7'] = "See your doctor. You may have CONGESTIVE HEART FAILURE (p. 570)."
    flowchart['N12'] = "Do you have new pets or new carpeting, has your carpet or upholstery been cleaned recently, or have you been inhaling the fumes of cleaning agents?"
    flowchart['A8'] = "You may be having an allergic reaction. See ALLERGIES TO AIRBORNE SUBSTANCES."
    flowchart['A9'] = "See your doctor if you cannot make a diagnosis from this chart."
    flowchart['A10'] = "See your doctor. Your problem is probably hyperventilation resulting from ANXIETY."

    # Define edges with conditions
    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N8", "No"),
        ("N2", "N3", "Yes"),
        ("N2", "N5", "No"),
        ("N3", "A1", "Yes"),
        ("N3", "N4", "No"),
        ("N4", "A2", "Yes"),
        ("N4", "A4", "No"),
        ("N5", "A3", "Yes"),
        ("N5", "N6", "No"),
        ("N6", "F1", "Yes"),
        ("N6", "N7", "No"),
        ("N7", "A10", "Yes"),
        ("N7", "N8", "No"),
        ("N8", "N9", "Yes"),
        ("N8", "A9", "No"),
        ("N9", "N10", "Yes"),
        ("N9", "N11", "No"),
        ("N10", "A5", "Yes"),
        ("N10", "A6", "No"),
        ("N11", "A7", "Yes"),
        ("N11", "N12", "No"),
        ("N12", "A9", "No"),
        ("N12", "A8", "Yes")
    ]

    return flowchart, edges_with_conditions

# Example output
    G = nx.DiGraph()
    G.add_nodes_from(flowchart.items())

    # Add edges to the graph
    for edge in edges_with_conditions:
        G.add_edge(edge[0], edge[1], condition=edge[2])

def Wheezing_Flowchart():
    # Define nodes (questions and advice)
    flowchart = {}
    flowchart['N1'] = "Did you begin wheezing within the past few hours?"
    flowchart['N2'] = "Have you coughed up mucus that is frothy and pink or white?"
    flowchart['A1'] = "EMERGENCY! Get medical help now. You may have CONGESTIVE HEART FAILURE."
    flowchart['N3'] = "Do you have a feeling of tightness in your chest, or do you feel as if you are suffocating?"
    flowchart['A2'] = "EMERGENCY! You may be having a severe asthma attack or hyperventilating."
    flowchart['A3'] = "See a doctor immediately. You may be having a mild asthma attack."
    flowchart['N4'] = "Is your temperature 100°F or higher?"
    flowchart['A4'] = "See your doctor. You may have ACUTE BRONCHITIS."
    flowchart['N5'] = "Do you wheeze on most days?"
    flowchart['N6'] = "Do you cough up gray or greenish-yellow phlegm on most days?"
    flowchart['A5'] = "See your doctor. You may have CHRONIC BRONCHITIS or EMPHYSEMA."
    flowchart['A6'] = "See your doctor if you are unable to make a diagnosis from this chart."

    # Define edges with conditions
    edges_with_conditions = [
        ("N1", "N2", "Yes"),
        ("N1", "N4", "No"),
        ("N2", "A1", "Yes"),
        ("N2", "N3", "No"),
        ("N3", "A2", "Yes"),
        ("N3", "A3", "No"),
        ("N4", "A4", "Yes"),
        ("N4", "N5", "No"),
        ("N5", "N6", "Yes"),
        ("N5", "A6", "No"),
        ("N6", "A5", "Yes"),
        ("N6", "A6", "No")
    ]

    return flowchart, edges_with_conditions

flowchart, edges_with_conditions = Wheezing_Flowchart()
G = nx.DiGraph()

# Add nodes
for node_id, text in flowchart.items():
    G.add_node(node_id, text=text)

# Add edges
for edge in edges_with_conditions:
    G.add_edge(edge[0], edge[1], condition=edge[2])

# To visualize the graph, use matplotlib or another graph visualization tool
