import colorama
from textblob import TextBlob
from colorama import Fore, Style
colorama.init()
print(f"{Fore.CYAN}⭐ welcome to sentiment spy⭐{Style.RESET_ALL}")
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
print(f"{Fore.CYAN}Hello Agent {user_name}! Type 'exit' to quit, 'reset' to clear, or 'history' to view chat.{Style.RESET_ALL}")
history =[]
while True:
    user_input = input(f"{Fore.green}{user_name}:{Style.RESET_ALL}").strip()
    if not user_input:
        print(f"{Fore.RED}PLese enter some text or a valid comand{Style.RESET_ALL}")
        continue
    if user_input.lower() == "exit":
        print(f"{Fore.CYAN}exiting sentiment spy farewell agent {user_name}{Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
    conversation_history.clear()
        print(f"{Fore.BLUE}conversation history cleared{user_name}{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "reset":
        if not history()
            print(f"{Fore.BLUE}no conversation history is ther{user_name}{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}conversation history{Style.RESET_ALL}")
            for idx, (text,polarity,sentiment_type) in enumerate
            (history,start=1):
                if sentiment_type == negative:
                        color=Fore.RED
                elif sentiment_type == positive:
                        color=Fore.GREEN
                else:
                        color = Fore.YELLOW
    blob=TextBlob(user_input)
    polarity=blob.sentiment.polarity
    if polarity>0.25:
                    sentiment_type="positive"
    if polarity<-0.25:
                    sentiment_type="negative"
    else:
                    sentiment_type="neutral"
print(f"{color}sentiment detected{sentiment_type}(Polarity: {polarity:.2f}){Style.RESET_ALL}")
history.append((user_input, polarity,sentiment_type))