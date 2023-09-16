import os
import magic
import shutil

def copy_and_rename_file(src_path, target_dir, new_name):
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Construct the destination path
    dest_path = os.path.join(target_dir, new_name)

    # Copy and rename the file
    shutil.copy(src_path, dest_path)

if __name__ == '__main__':

    all_endings = {'no_classification_yet' : 0}

    shutil.rmtree('cleaned')
    os.makedirs('cleaned')

    for file in os.listdir('files'):
        file_end = file.split('.')
        
        if len(file_end) == 1:
            # No classification
            # mime = magic.from_file(f"../data/{file}")
            mime = magic.from_file(f"files/{file}", mime=True)
            # print(f'Name: {file_end}, {mime}')
            if mime == 'text/plain':
                target_dir = f'cleaned/no_ext'
                copy_and_rename_file(f"files/{file}", target_dir, file_end[0] + '.' + mime.split('/')[1])
                continue
            # else: 
            #     # print(file_end[0] + '.' + mime.split('/')[1])
            #     pass
            
            if mime.split("/")[1] in all_endings.keys():
                all_endings[mime.split("/")[1]] += 1
            else:
                all_endings[mime.split("/")[1]] = 1

            target_dir = f'cleaned/{mime.split("/")[1]}'

            all_endings['no_classification_yet'] += 1
            copy_and_rename_file(f"files/{file}", target_dir, file_end[0] + '.' + mime.split('/')[1])

        elif len(file_end) == 2:
            if file_end[1] in all_endings.keys():
                all_endings[file_end[1]] += 1
            else:
                all_endings[file_end[1]] = 1

            # We should maybe check if the file endings are actually correct

            target_dir = f'cleaned/{file_end[1]}'
            copy_and_rename_file(f"files/{file}", target_dir, file)

        elif len(file_end) > 2:
            print('what' + str(file_end))

    print(all_endings)