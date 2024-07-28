import os
import json
import requests


class LabelStudioAPI:
    def __init__(self) -> None:
        self.HOST = os.getenv('LABEL_STUDIO_API_HOST')
        self.TOKEN = os.getenv('LABEL_STUDIO_TOKEN')

    @staticmethod
    def get_token(cookie):
        url = f"{os.getenv('LABEL_STUDIO_HOST')}/api/current-user/token"
        payload = {}
        headers = {
            'Cookie': cookie
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return json.loads(response.text)


    def get_user_info(self,):
        url = f"{self.HOST}/api/current-user/whoami"
        payload = {}
        headers = {
            'Authorization': f'Token {self.TOKEN}',
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return json.loads(response.text)


    def get_all_projects(self):
        url = f'{self.HOST}/api/projects/'
        headers = {
            'Authorization': f'Token {self.TOKEN}',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            projects = response.json()
            return projects
        else:
            print('Error fetching projects. Status code:', response.status_code)
            return None

    def get_project_tasks(self,project_id,page=1,page_size=10):
        url = f"{self.HOST}/api/projects/{project_id}/tasks/"
        payload = {
            "page":page,
            "page_size":page_size
        }
        headers = {
        'Authorization': f'Token {self.TOKEN}',
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        return json.loads(response.text)

    def import_image(self, project_id,image_path):
        url = f"{self.HOST}/api/projects/{project_id}/import"
        payload = {"commit_to_project":True}
        files=[
            (os.path.basename(image_path),(os.path.basename(image_path),open(image_path,'rb'),'image/jpeg'))
            ]
        headers = {
            'Authorization': f'Token {self.TOKEN}',
            }
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        return json.loads(response.text)

    def delete_task(self,task_id):
        url = f"{self.HOST}/api/tasks/{task_id}"
        payload = {}
        headers = {
            'Authorization': f'Token {self.TOKEN}',
            }
        response = requests.request("DELETE", url, headers=headers, data=payload)
        return json.loads(response.text)

    def create_project(self,label_config):
        url = f"{self.HOST}/api/projects"
        payload = label_config
        headers = {
            'Authorization': f'Token {self.TOKEN}',
            }
        response = requests.request("POST", url, headers=headers, data=payload)
        return json.loads(response.text)


    def create_image_classification_project(self,title,description,choices):
        choices_config = ''.join([f'<Choice value="{choice}"/>' for choice in choices])
        label_config = {
        "title": title,
        "description": description,
        "label_config": f'<View><Image name="image" value="$image"/><Choices name="choice" toName="image">{choices_config}</Choices></View>'
        }
        response = self.create_project(label_config)
        return response


    def create_text_classification_project(self,title,description,choices,text_header="Choose Text Class"):
        choices_config = ''.join([f'<Choice value="{choice}"/>' for choice in choices])
        label_config = {
        "title": title,
        "description": description,
        "label_config": f'<View><Text name="text" value="$text"/><View style="box-shadow: 2px 2px 5px #999; padding: 20px; margin-top: 2em; border-radius: 5px;"><Header value="{text_header}"/><Choices name="choice" toName="text" choice="single" showInLine="true">{choices_config}</Choices></View></View>'
        }
        response = self.create_project(label_config)
        return response


if __name__ == "__main__":
    ls = LabelStudioAPI()

    # user_info = ls.get_user_info()

    # projects = ls.get_all_projects()
    # projects_dict = {}
    # for proje in projects['results']:
    #     print(f"PROJECT ID {proje['id']} \t SIZE {proje['task_number']} \t  TITLE {proje['title']}")
    #     projects_dict.update({proje['title']:proje['id']})

    # project_tasks = ls.get_project_tasks(projects_dict['gender_age_classification'])

    # image_path = "/home/mahdi/Pictures/eeee.jpeg"
    # response = ls.import_image(projects_dict['gender_age_classification'],image_path)


    # project_label_config ={
    #     "title": "python",
    #     "description": "test test test ",
    #     "label_config": '<View><Image name="image" value="$image"/><Choices name="choice" toName="image"><Choice value="Adult content"/><Choice value="Weapons" /><Choice value="Violence" /></Choices></View>'
    #     }
    # project_create_response = ls.create_project(project_label_config)

    project_create_response = ls.create_image_classification_project(title="image_test",description="1234",choices=['a','b','c'])
    project_create_response = ls.create_text_classification_project(title="text_test",description="1234",choices=['a','b','c'])

    print("test")