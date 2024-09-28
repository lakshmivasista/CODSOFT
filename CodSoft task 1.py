def Her_Safe():
    print("Her_Safe: Welcome to HerSafe.You're not alone, and we're here to support you.")
    
    while True:
        user_input = input("You: ").lower()
    
        if "hello" in user_input or "hi" in user_input:
            print("Her_Safe: Hi! you're safe here, what brings you here today?")
        elif "safety guidelines" in user_input:
            print("Her_Safe: Here are some safety guidelines:\n"
                  "1. Always be aware of your surroundings.\n"
                  "2. Trust your instincts and avoid isolated areas.\n"
                  "3. Share your location with a trusted family or friend member.\n"
                  "4. Keep your phone charged and accessible.\n"
                  "5. set boundaries,clearly communicate your limits to others.")
        elif "emergency contacts" in user_input:
            print("Her_Safe: In case of an emergency, you can reach out to the following contacts:\n"
                  "1. Police: 100\n"
                  "2. Women's Helpline: 1091\n"
                  "3. Emergency Services: 112\n"
                  "4. Trusted Friend/Family: (Add your own emergency contact numbers)")
        elif "self-defense" in user_input:
            print("Her_Safe: It's important to know some basic self-defense techniques:\n"
                  "1. Aim for vulnerable areas like the eyes, nose, and groin.\n"
                  "2. Use everyday objects like keys or pens as weapons.\n"
                  "3. Shout as louder as possible to attract attention.\n"
                  "4. Take self defense classes if possible.")
        elif "mental health support" in user_input:
            print("Her_Safe: Mental health is crucial. Here are some resources:\n"
                  "1. National Mental Health Helpline: 1800-599-0019\n"
                  "2. Speak to a trusted counselor or therapist.\n"
                  "3. Practice self-care and reach out to friends or support groups.")
        elif "bye" in user_input or "exit" in user_input or "thankyou" in user_input:
            print("Her_Safe: Goodbye! Stay safe and take care.")
            break
        else:
            print("Her_Safe: I'm here to help. You can ask about safety tips, emergency contacts, self-defense, or mental health support.")
Her_Safe()