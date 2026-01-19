from telegram import *
import telegram.ext as tex
import asyncio
import datetime as dt
from database import *

# TOKEN = "<ENTER YOUR BOT TOCKEN HERE>"
# BOT_USERNAME = "<BOT USERNAME>"

update = tex.Updater(TOKEN,  asyncio.Queue())


def calculate_age(dob: str) -> int:
    current_date = str(dt.date.today()).split("-")
    year = int(current_date[0])
    age = year - int(dob.split('-')[2])
    month = int(dob.split('-')[1])
    if month > int(current_date[1]):
        age -= 1
    return age

NAME, EMAIL, PHONE, DOB = range(4)

async def ask_name(update: Update, context: tex.CallbackContext) -> int:
    await update.message.reply_text('What is your name?')
    return NAME

async def ask_email(update: Update, context: tex.CallbackContext) -> int:
    name = update.message.text
    context.user_data['name'] = name
    await update.message.reply_text('What is your email?')
    return EMAIL

async def ask_phone(update: Update, context: tex.CallbackContext) -> int:
    email = update.message.text
    context.user_data['email'] = email
    await update.message.reply_text('What is your phone number?')
    return PHONE

async def ask_dob(update: Update, context: tex.CallbackContext) -> int:
    phone = update.message.text
    context.user_data['phone'] = phone
    await update.message.reply_text('What is your date of birth (dd-mm-yyyy)?')
    return DOB

async def save_data(update: Update, context: tex.CallbackContext) -> int:
    dob = update.message.text
    context.user_data['dob'] = dob
    # Save the user data to your database
    user_info = {
        'name': context.user_data['name'],
        'email': context.user_data['email'],
        'phone': context.user_data['phone'],
        'dob': context.user_data['dob'],
        'age': calculate_age(str(context.user_data['dob']))
        }
    global coustomer_data
    coustomer_data = user_info
    # Save user_info to your database
    await update.message.reply_text('Thank you for signing up!')
    return tex.ConversationHandler.END

async def cancel(update: Update, context: tex.CallbackContext) -> int:
    await update.message.reply_text('Sign-up process cancelled.')
    return tex.ConversationHandler.END


#Returns the data from user message
async def get_data(update: Update, context: tex.CallbackContext) -> dict:
    context.user_data["in_signup_process"] = True
    
    username = update.message.from_user.username
    chat_id = update.message.chat.id 
    message_id = update.message.message_id
    full_name = f"{update.message.chat.first_name} {update.message.chat.last_name}"
    return {"ID": chat_id, "Username": username} + coustomer_data + {"Message_Id": message_id}


#CommandHandlers
async def start(update, context):
    #If Exixting User
    await update.message.reply_text('Welcome! This is The BANK ATM you have $5000 in your account how can I asist you')
    

async def help(update, context):
    await update.message.reply_text('/start -> Start chatting with bot \n' +
                                    '/help -> Get Bot help \n' +
                                    '/menu -> Perform Actions \n' +
                                    '/policy -> BANK policies must read')

async def policy(update, context):
    await update.message.reply_text("• This is a Virtual Bank and it is completly handeled by Bots an AIs \n\n" +
                                    "• You can't make any withdrawl to any other bank. \n\n" +
                                    "• You can't add any money from you real bank account \n\n" +
                                    "• This is a Virtual Bank and it has virtual curreny as dollar because it is globally accepted \n\n " +
                                    "• We recomdate you to keep updated with BANK's Policies we are updating it on regular basis." )

async def menu(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Balance 💸", callback_data='balance'),
            InlineKeyboardButton("Send", callback_data='pay'),
        ],

        [
            InlineKeyboardButton("Find Friend", callback_data='search'),
            InlineKeyboardButton("Sing Up", callback_data='sing_up'),
        ],
    ]
    # Create a message with the inline keyboard
    message = "How can I help you"
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=message, reply_markup=InlineKeyboardMarkup(keyboard))
    query: str = update.callback_query
    print(query)
    return query  


#Responses
def handle_response(update: Update, text: str)  -> str:
    # get_data(update)
    if "hello" == text.lower() or "hi" == text.lower():
        return f"Hello {update.message.from_user.username}!" 
    
    elif "bye" == text.lower() or "Goodbye" == text.lower():
        return f"Nice to meet you bye"
    
    else:
        return  "Please enter some valid commands or refer /menu"
    
#Handles the unwanted messages
async def handle_message(update: Update, context: tex.ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    if message_type == "group":
        if BOT_USERNAME in  text:
            new_text: str = text.replace(BOT_USERNAME,"").strip()
            response: str = handle_response(new_text)

        else:
            return
    else:
        if context.user_data.get("in_signup_process", False):
            # User is in sign-up process, let get_data handle the response
            user_info = await get_data(update, context)
            print(user_info)
        else:
            response: str = handle_response(update, text)
            await update.message.reply_text(response)

# Give Buttons Response in menu
async def handle_query(update: Update, context: tex.CallbackContext):
    query: str = update.callback_query.data
    await update.callback_query.answer()
    if query == "sing_up":
        user_info = await get_data(update, context)
        print(user_info)
        context.user_data["in_signup_process"] = False
    elif query == "pay":
        print(query)
    elif query == "balance":
        print(query)
    elif query == "search":
        print(query)
    else:
        print(query)


async def error(update: Update, context: tex.ContextTypes.DEFAULT_TYPE):
    print(f"Update: {update} Context: {context} \n\n Error: {context.error}")


if __name__ == "__main__":
        application = tex.Application.builder().token(TOKEN).build()

        application.add_handler(tex.CommandHandler('start', start))
        application.add_handler(tex.CommandHandler('help', help))
        application.add_handler(tex.CommandHandler('policy', policy))
        application.add_handler(tex.CommandHandler('menu', menu))

        conv_handler = tex.ConversationHandler(
        entry_points=[tex.CallbackQueryHandler(menu, pattern='sing_up')],
        states={
            NAME: [tex.MessageHandler(tex.filters.TEXT, ask_name)],
            EMAIL: [tex.MessageHandler(tex.filters.TEXT, ask_email)],
            PHONE: [tex.MessageHandler(tex.filters.TEXT, ask_phone)],
            DOB: [tex.MessageHandler(tex.filters.TEXT, ask_dob)]
        },
        fallbacks=[tex.CommandHandler('cancel', cancel)]
                                        )

        application.add_handler(conv_handler)
        application.add_handler(tex.CallbackQueryHandler(handle_query))
        application.add_handler(tex.MessageHandler(tex.filters.TEXT & ~tex.filters.COMMAND, handle_message))

        app =  tex.Application.builder().token(TOKEN).build()
        # Message
        app.add_handler(tex.MessageHandler(tex.filters.Text, handle_response))

        # Error
        app.add_error_handler(error)

        print("Bot Started Polling...")
        application.run_polling()

