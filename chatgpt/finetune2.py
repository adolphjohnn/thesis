import openai

def open_file(filepath):
	with open(filepath,'r', encoding='utf-8') as infile:
		return infile.read()

def save_file(filepath, content):
	with open(filepath,'a', encoding='utf-8') as outfile:
            outfile.write(content)

api_key = open_file('apikey.txt')
openai.api_key = api_key

file_id ="file-MaEllHhvLOnatwSQo5dxdOi9"

model_name = "gpt-3.5-turbo-0613"

response = openai.FineTuningJob.create(
	training_file = file_id,
	model = model_name
	
)

job_id = response['id']

print(f"Finr-tuning job created successfully with ID:{job_id}")