from xposedornot import XposedOrNot
#Import the XposedOrNot class from the xposedornot module.

xon = XposedOrNot() #Define the xon variable as an instance of the XposedOrNot class.




languages = str(input("Enter your language (en/fr): ")) #Language selection system, only English and French are supported for now.

while languages not in ["en", "fr"]:
    #Error handling. Might be improved by using regex in the future.

    print("Invalid language selection. Please choose 'en' for English or 'fr' for French.")
    languages = str(input("Enter your language (en/fr): "))

if languages == "en":
    print("") #Jumping line for better readability.

    print("Welcome to the XposedOrNot breach checker!")
    print("This tool allows you to check if your email or password has been exposed in any known data breaches.")
    print("Please enter your email address below to get started.")

    print("") #Jumping line for better readability.

    print("Enter your email to check for breaches : ")
    #Allow user to test the program with a default email if they don't want to enter their own.
    email=str(input("Or you can press Enter to use the default email to test (test@example.com) : ") or "test@example.com")

    analytics = xon.breach_analytics(email)
    NbrOfBreaches = analytics.exposures_count

    print(f"Total exposures: {NbrOfBreaches}")

        



else :
    print("Bienvenue dans le vérificateur de violations XposedOrNot !")
    print("Cet outil vous permet de vérifier si votre e-mail ou mot de passe a été exposé dans des violations de données connues.")
    print("Veuillez entrer votre adresse e-mail ci-dessous pour commencer.")
    email=str(input("Entrez votre e-mail pour vérifier les fuites : "))
    print("Utiliser l'anglais pour les tests de développement, car la traduction française n'est pas encore complète.")



