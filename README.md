# aitecell

## Endpoints

<details>
    <summary>API's: <code>https://aitecell.herokuapp.com/api</code></summary>
    "api": "https://aitecell.herokuapp.com/api/",
    "eventtypes": "https://aitecell.herokuapp.com/api/eventtypes/?format=json",
    "events": "https://aitecell.herokuapp.com/api/events/?format=json",
    "events/upcoming_events": "http://127.0.0.1:8000/api/events/upcoming_events/?format=json",
    "events/live_events": "http://127.0.0.1:8000/api/events/live_events/?format=json",
    "events/past_events": "http://127.0.0.1:8000/api/events/past_events/?format=json",
    "latestupdates": "https://aitecell.herokuapp.com/api/latestupdates/?format=json",
    "documents": "https://aitecell.herokuapp.com/api/documents/?format=json",
    "videos": "https://aitecell.herokuapp.com/api/videos/?format=json",
    "startups": "https://aitecell.herokuapp.com/api/startups/?format=json",
    "categories": "https://aitecell.herokuapp.com/api/categories/?format=json",
    "people": "https://aitecell.herokuapp.com/api/people/?format=json",
    "people/ecell_team": "http://127.0.0.1:8000/api/people/ecell_team/?format=json",
    "people/ecell_team_alumni": "http://127.0.0.1:8000/api/people/ecell_team_alumni/?format=json",
    "people/alumni_entrepreneur": "http://127.0.0.1:8000/api/people/alumni_entrepreneur/?format=json",
    "links": "https://aitecell.herokuapp.com/api/links/?format=json",
    "internships": "https://aitecell.herokuapp.com/api/internships/?format=json",
    "internships/is_active": "http://127.0.0.1:8000/api/internships/is_active//?format=json",
    "collaboration": "https://aitecell.herokuapp.com/api/collaboration/?format=json",
</details>


<details>
<summary>Admin panel: <code>https://aitecell.herokuapp.com/admin</code></summary>
    
    username: admin
    password: admin
    
</details>


## Models

<details>
<summary>1. Event Model</summary>
    
    1. title  
    2. description  
    3. datetime_from  
    4. datetime_to  
    5. image_url  
    6. meet_url
    7. type of event (event/visit/session)
    7. others field
    8. multiple files attachment
    9. comments/questions related to the event
</details>

<details>
<summary>2. Latest updates</summary>
    
    1. update heading  
    2. datetime_from  
    3. datetime_to  
    4. imp_post url  
    
    is_active()
</details>

<details>
<summary>3. documents to be uploaded on website/including newsletter/policy/rules/etc</summary>
    
    1. doc's heading
    2. doc's url
    3. doc's description
    4. doc's image
</details>

<details>
<summary>4. youtube videos section</summary>
    
    1. video's heading
    2. video's url
    3. video's description
</details>


<details>
<summary>5. startup initiatives</summary>
    
    1. startup's heading
    2. startup's url
    3. startup's description
    4. startup's image
</details>

<details>
<summary>6. people</summary>
    
    1. Name
    2. Designation
    3. Image
    4. Description
    5. Social links (linkedin / instagram / flexible to add more)
    6. Category (alumni entrepreneur/industrial mentor/faculty mentor/team member/advisors/)
</details>

<details>
<summary>7. Links</summary>
    
    1. heading
    2. url
    3. description
    4. logo url
</details>

<details>
<summary>8. Internships</summary>
    
    1. heading
    2. company url
    3. description/body)
    4. Poster/image
    5. apply link
    6. deadline
</details>
