import pandas as pd
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# ==============================
# STEP 1: Load External Dataset
# ==============================
# This function loads the dataset from a CSV file.
# It returns a pandas DataFrame containing Indian states and their tourism places.
def load_dataset():
    try:
        df = pd.read_csv("indian_states_tourism_places.csv")
        print("✅ Dataset loaded successfully!")
        return df
    except FileNotFoundError:
        print("❌ Error: 'indian_states_tourism_places.csv' not found in the current directory.")
        return None

# Load dataset globally so it's accessible to all functions
df = load_dataset()

# ==============================
# STEP 2: Define Bot Commands
# ==============================
# This function handles the /start command.
# It sends a welcome message when a user starts the bot.
def start(update, context):
    update.message.reply_text(
        "👋 Welcome to the *Incredible India Tourism Bot* 🇮🇳\n\n"
        "Send me the name of any *Indian State* and I’ll tell you its top tourism places!\n\n"
        "Example: `Kerala`, `Rajasthan`, `Goa`",
        parse_mode='Markdown'
    )

# ==============================
# STEP 3: Message Handling Function
# ==============================
# This function handles user text messages.
# It searches for the entered state name in the dataset and replies with the corresponding tourism places.
def get_tourism_places(update, context):
    # If dataset failed to load
    if df is None:
        update.message.reply_text("⚠️ Dataset not loaded. Please contact the administrator.")
        return

    # Get user input and normalize capitalization
    user_input = update.message.text.strip().title()

    # Search for the state in the dataset
    match = df[df['State'] == user_input]

    # If a match is found, send the tourism places
    if not match.empty:
        places = match.iloc[0]['Tourism Places']
        response = f"🌍 *Top Tourism Places in {user_input}:*\n\n{places}"
    else:
        # If no match found, send an error message
        response = (
            "⚠️ Sorry! I couldn’t find that state.\n\n"
            "Please check the spelling or try another Indian state name."
        )

    # Send the response message back to the user
    update.message.reply_text(response, parse_mode='Markdown')

# ==============================
# STEP 4: Initialize Telegram Bot
# ==============================
# This function sets up the bot, connects to Telegram using your bot token,
# and defines the message handlers for different commands and inputs.
def main():
    # Replace with your actual Telegram bot token from BotFather
    TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

    # Create the bot instance
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register the /start command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Register message handler for all text messages (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_tourism_places))

    # Start polling to listen for messages
    print("🤖 Bot is running... Press Ctrl+C to stop.")
    updater.start_polling()

    # Keep the bot running until manually stopped
    updater.idle()

# ==============================
# STEP 5: Run the Bot
# ==============================
# Entry point of the script.
if __name__ == '__main__':
    main()
