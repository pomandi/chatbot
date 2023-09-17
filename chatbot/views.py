from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai

openai.api_key = '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'

def home(request):
    return HttpResponse("Hoşgeldiniz!")

def chatbot_response(user_input):
    prompt = {
        'messages': [
            {'role': 'system', 'content': 'Şirket hakkında bilgi: Şirketimiz 1990 yılında kurulmuştur. Ürünlerimiz arasında Takim elbise, Gomlek,Kravat bulunmaktadır.'},
            {'role': 'system', 'content': 'Mağazamızın açılış saatleri hafta içi 09:00 - 18:00, hafta sonu 10:00 - 16:00 arasındadır.'},
            {'role': 'user', 'content': user_input}
        ]
    }
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt['messages']
    )
    message = response.choices[0].message['content'].strip()
    return message

def chat_view(request):
    return render(request, 'chat.html')

@csrf_exempt
def get_response(request):
    user_message = request.POST.get('message')
    bot_response = chatbot_response(user_message)
    return JsonResponse({'message': bot_response})
