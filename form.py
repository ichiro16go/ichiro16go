import random
import requests

# GoogleフォームのURL（フォームごとに異なる部分を指定）
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLScrDqroKEHj2dLWVFAws0Gfo1CoMeFcBdo5wFtoI22Bosr6mw/formResponse'

weights1 = [10, 1, 2, 4]
weights2 = [3, 14, 5, 19]

for _ in range(50):
    # フォームの各フィールドに対応するentry ID
    form_data = {
        'entry.671711276': random.choices([
            'Building Disaster-Resistant Infrastructure',
            'Implementing Early Warning Systems',
            'Community Education and Engagement',
            'Utilizing Advanced Technology',
        ], weights=weights1, k=1)[0],
        'entry.2048028182': random.choices([
            'Focus on Resilience in Urban Design',
            'Cutting-Edge Technology for Early Warnings',
            'Strong Emphasis on Community Preparedness',
            'Innovative Environmental Policies'
        ], weights=weights2, k=1)[0],
    }
    response = requests.post(form_url, data=form_data)
    if response.status_code == 200:
        print("フォームが送信されました")
    else:
        print("送信に失敗しました:", response.status_code)
