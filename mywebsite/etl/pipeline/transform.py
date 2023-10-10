import pandas as pd

def clean_text_file(file_name):
    cleaned_data = []
    
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            line_data = line.strip().split(' ')
            
            date = line_data[0][:5]
            
            if len(line_data) >= 6 and '-' in line_data[3]:
                opponent = line_data[1]
                result = line_data[2]
                scores = line_data[3].split('-')
                location = line_data[4]
                overall_record = line_data[5].split('-')
                division_record = line_data[6].split('-')

                cleaned_data.append([date, opponent, result, scores[0], scores[1], location, overall_record[0], overall_record[1], division_record[0], division_record[1]])

            elif len(line_data) >= 6 and ('W' in line_data[3] or 'L' in line_data[3]):
                opponent = line_data[1] + ' ' + line_data[2]
                result = line_data[3]
                scores = line_data[4].split('-')
                location = line_data[5]
                overall_record = line_data[6].split('-')
                division_record = line_data[7].split('-')

                cleaned_data.append([date, opponent, result, scores[0], scores[1], location, overall_record[0], overall_record[1], division_record[0], division_record[1]])
    
    # Convert cleaned_data to a pandas DataFrame
    data = pd.DataFrame(cleaned_data, columns=['date', 'opponent', 'result', 'ny_score', 'opponent_score', 'location', 'total_wins', 'total_losses', 'divisional_wins', 'divisional_losses'])
    return data