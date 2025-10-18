import requests
import sys
import html2text
import os

def get_all_problems_map():
    """
    Fetches all problems from LeetCode and returns a map of
    questionId -> titleSlug.
    """

    url = "https://leetcode.com/api/problems/all/"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://leetcode.com/problemset/all/'
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        raise Exception("Failed to fetch problem list.")
        
    data = response.json()

    problem_list = data['stat_status_pairs']
    
    id_to_slug_map = {
        str(problem['stat']['frontend_question_id']): problem['stat']['question__title_slug']
        for problem in problem_list
    }
    
    return id_to_slug_map

def get_problem_data(slug):
    """Fetches problem data from LeetCode's GraphQL API using the titleSlug."""

    url = "https://leetcode.com/graphql"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Referer': f'https://leetcode.com/problems/{slug}/'
    }
    query = """
    query questionContent($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        title
        content
      }
    }
    """

    variables = {"titleSlug": slug}
    payload = {"query": query, "variables": variables}
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if 'errors' in data:
            raise Exception(f"Error from LeetCode API: {data['errors']}")
        return data['data']['question']
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")

def format_problem_to_markdown(problem_data):
    """Converts the problem data dictionary into a formatted Markdown string."""

    h = html2text.HTML2Text()
    
    # Disable automatic line wrapping to keep code blocks intact
    h.body_width = 0
    
    # Extract details
    question_id = problem_data['questionId']
    title = problem_data['title']
    html_content = problem_data['content']
    
    # Convert HTML to Markdown
    markdown_content = h.handle(html_content)
    
    # Clean up extra newlines that html2text often adds inside <pre> blocks
    markdown_content = markdown_content.replace('\n    \n', '\n')

    # Assemble the final Markdown string
    markdown_output = (
        f"# {question_id}. {title}\n\n"
        f"---\n\n"
        f"{markdown_content}"
    )
    
    return markdown_output

def makeProblemDirectory(dirname):
    """Creates a directory for the problem if it doesn't already exist."""

    if not os.path.exists(dirname):
        os.makedirs(dirname)
        print(f"Directory '{dirname}' created.")

        return True
    else:
        print(f"Directory '{dirname}' already exists.")

        return False
    
def makeSolutionFile(filename, language):
    """Creates a solution file if it doesn't already exist."""
        
    languagesCodeExtensions = {
        "python": "py",
        "java": "java",
        "cpp": "cpp",
        "c": "c",
        "javascript": "js",
        "ruby": "rb",
        "go": "go",
        "csharp": "cs",
        "swift": "swift",
        "kotlin": "kt"
    }

    code_filename = f"{filename}.{languagesCodeExtensions.get(language, 'java')}"

    if not os.path.exists(code_filename):
        try:
            code_file =  open(code_filename, 'w', encoding='utf-8')
        except Exception as e:
            print(f"Error creating code file '{code_filename}': {e}")
        finally:
            code_file.close()

        print(f"✅ Created code file '{code_filename}' for solution.")
    else:
        print(f"Code file '{code_filename}' already exists. Skipping creation.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python your_script_name.py <question_number>")
        sys.exit(1)

    question_id_input = sys.argv[1]

    try:
        print("Fetching problem list to create ID-to-Slug map...")
        problem_map = get_all_problems_map()

        print("Map created successfully.")

        if question_id_input in problem_map:
            target_slug = problem_map[question_id_input]

            dirName = question_id_input + '-' + '-'.join([word.capitalize() for word in target_slug.split('-')])

            problem_data = get_problem_data(target_slug)

            print("Problem details fetched successfully. Formatting to Markdown...")
            
            markdown_output = format_problem_to_markdown(problem_data)

            print('Formatting complete.')
            print(f'Do you want to save the formatted problem to directory {dirName}? (y/n): ', end='')

            user_input = input().strip().lower()
            if user_input == 'y':
                makeProblemDirectory(dirName)
                os.chdir(dirName)

                filename = "README.md"
            else:
                filename = f"{question_id_input}-{target_slug}.md"
                print(f"Saving to current directory as '{filename}'")
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(markdown_output)
            
            print(f"\n✅ Successfully saved formatted problem to '{filename}'")

            print('Do you want to create a solution file? (y/n): ', end='')
            user_input = input().strip().lower()
            if user_input == 'y':
                print('Do you want to create the solution file in Java? (default is Java) (y/n): ', end='')
                lang_input = input().strip().lower()
                
                if lang_input != 'y':
                    print('Enter the programming language (e.g., python, cpp, javascript): ', end='')
                    language = input().strip().lower()
                else:
                    language = "java"

                makeSolutionFile(dirName, language)
                print("You can now implement your solution in the created file.✅")
            else:
                print("Skipping solution file creation.")

            print('####################################################')
            print("Process completed successfully. Happy coding!")
            print('made by mar1shell, check marouane.net for more!')
            print('####################################################')
        else:
            print(f"Error: Question ID '{question_id_input}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")