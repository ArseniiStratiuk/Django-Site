# Django Website Blog using JavaScript, Python, and SQL

#### Video Demo:  https://youtu.be/cuiRF7mrngw

#### Description: The Django Website Blog is an educational project designed to demonstrate the capabilities of the Django web framework. This project implements a fully functional blog site with features such as viewing, searching, and liking various articles. Additionally, it includes a system for user profiles, comments, and other common website functionalities like chat

## Project Structure

The project is organized into several key components, each responsible for different aspects of the website's functionality. Below is a detailed explanation of each file and its purpose:

### `views.py`

This file contains the logic for handling requests and returning responses. It includes class-based views and function-based views for various functionalities such as displaying posts, handling user registration, managing user profiles, and handling private messages. Key views include:

- `PostListMain`: Displays a list of blog posts with pagination.
- `ShowPost`: Displays a single post in detail, including comments and like/save functionality.
- `UserRegistration`: Handles user registration.
- `profile`: Displays and updates the user's profile.
- `like_post` and `save_post`: Handle liking and saving posts.
- `load_messages_home`: Loads the home page for private messages.
- `load_messages`: Loads messages between the logged-in user and another user.
- `load_msgAJAX`: Handles AJAX requests for loading and sending messages.
- `send_message`: Handles sending messages between users.

### `models.py`

This file defines the database models for the project. It includes models for `Profile`, `Category`, `Post`, `Comment`, and `Message`. Each model includes fields and methods relevant to its purpose. For example, the `Post` model includes methods to get the number of views and likes, while the `Message` model includes fields for sender, receiver, and text content.

### `forms.py`

This file contains the forms used in the project. It includes forms for user registration, profile updates, and post creation. These forms handle user input and validation, ensuring that the data submitted by users is correctly processed.

### `admin.py`

This file registers the models with the Django admin site, allowing for easy management of the database through the admin interface. It includes customizations for displaying and managing `Profile`, `Category`, `Post`, `Comment`, and `Message` models in the admin panel.

### `urls.py`

This file maps URLs to views. The project is divided into different parts, each with its own `urls.py` file to handle specific functionalities:

#### `blog/urls.py`

Handles the main blog functionality, including viewing, searching, and interacting with posts.

#### `chat/urls.py`

Handles the chat functionality, including loading messages and handling AJAX requests.

#### `learnsite/urls.py`

The main URL configuration file that includes paths for the blog, chat, captcha, and admin functionalities.

### Templates

The project uses HTML templates to render the frontend. Key templates include:

- `post_view.html`: Displays a single post with its details, comments, and like/save buttons.
- `privatechat.html`: Displays the private chat interface with a list of users and the chat messages.
- `blog_main.html`: Displays the main blog page with a list of posts and a carousel of featured posts.
- `login.html`: Provides the login form for users to authenticate themselves.
- `register.html`: Provides the registration form for new users to create an account.
- `profile.html`: Displays the user's profile information and allows them to update their details.
- `category.html`: Displays posts filtered by category, including a sidebar for category navigation.
- `look_profile.html`: Displays the profile of another user, showing their avatar and about information.
- `navbar.html`: Contains the navigation bar that is included across various pages for consistent navigation.
- `footer.html`: Contains the footer section with additional information and scripts for the website.

### Static Files

The project includes static files such as CSS and JavaScript to enhance the frontend. Materialize CSS is used for styling, providing a modern and responsive design.

### Additional Features

- **User Authentication**: The project includes user authentication using Django's built-in authentication system. Users can register, log in, and manage their profiles.
- **Comments**: Users can comment on posts, and the comments are displayed below each post.
- **Likes and Saves**: Users can like and save posts, and the number of likes and saves is displayed on each post.
- **Search**: Users can search for posts using a search bar.
- **Pagination**: The list of posts is paginated to improve usability.

## Design Choices

Several design choices were made to enhance the functionality and user experience of the project:

- **Class-Based Views**: Class-based views were used for most of the views to take advantage of Django's built-in functionality and to keep the code organized.
- **Materialize CSS**: Materialize CSS was chosen for its modern design and ease of use, allowing for a responsive and visually appealing frontend.
- **User Context**: A mixin was used to add user-specific context to the views, ensuring that the user's likes, saves, and other interactions are displayed correctly.

## Conclusion

The Django Website Blog project is a comprehensive demonstration of the capabilities of the Django web framework. It includes a wide range of features commonly found in modern web applications, such as user authentication, comments, likes, and search functionality. The project is well-organized and makes use of best practices in Django development, making it a valuable learning resource for anyone interested in web development.

## Acknowledgements

I would like to extend my heartfelt appreciation to the CS50 staff for their incredible course. The knowledge and skills gained from CS50x, especially the sections on Flask, Python, and cybersecurity, were invaluable in the development of this project. Thank you for providing such a comprehensive and engaging learning experience.
