.. _en-index:

Home
=========

.. raw:: html

    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

        body {
            font-family: 'Roboto', sans-serif;
            background-color: #f0f2f5;
        }

        .jumbotron {
            background: linear-gradient(135deg, #2c3e50, #4ca1af);
            color: white;
            text-align: center;
            padding: 3rem 2rem;
            border-radius: 20px;
            margin-bottom: 3rem;
        }

        .jumbotron h1 {
            font-size: 2.8rem;
            margin-bottom: 1rem;
        }

        .jumbotron p {
            font-size: 1.1rem;
            margin: 0.5rem auto;
            max-width: 800px;
        }

        .card-deck {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
            padding: 0 2rem 2rem;
        }

        .card {
            flex: 1 1 280px;
            border-radius: 15px;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
            background-color: #ffffff;
            transition: transform 0.3s, box-shadow 0.3s;
            padding: 1.5rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
        }

        .card-title {
            font-size: 1.4rem;
            color: #2c3e50;
            margin-bottom: 0.8rem;
        }

        .card-text {
            font-size: 1rem;
            color: #555;
            flex-grow: 1;
        }

        .btnn {
            display: inline-block;
            margin-top: 1.5rem;
            padding: 0.6rem 1.2rem;
            background-color: #4ca1af;
            color: white;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: background-color 0.3s;
            text-align: center;
        }

        .btnn:hover {
            background-color: #2c3e50;
        }
    </style>

    <div class="jumbotron">
        <h1 class="display-4">Welcome</h1>
        <p>I'm <strong>John GABARY</strong>, a certified actuary passionate about <strong>modern actuarial science</strong>, <strong>data science</strong>, and <strong>designing explainable and accessible models</strong>.</p>
        <p>My mission: <em>to bridge the gap between mathematical theory, programming, and real-world decision-making.</em></p>
        <p>Through my work, I combine statistical rigor, digital tools, and creativity to deliver transparent, high-performance, and impactful models.</p>
    </div>

    <div class="card-deck">
        <div class="card">
            <div class="card-body">
                <h4 class="card-title">About Me</h4>
                <p class="card-text">Learn about my background, core values, and vision for an actuarial profession that's practical, impactful, and forward-thinking.</p>
                <a href="about/index.html" class="btnn">Learn More</a>
            </div>
        </div>

        <div class="card">
            <div class="card-body">
                <h4 class="card-title">My Resume</h4>
                <p class="card-text">Discover my education, experience, technical skills, and certifications, all in one place.</p>
                <a href="cv/index.html" class="btnn">View CV</a>
            </div>
        </div>

        <div class="card">
            <div class="card-body">
                <h4 class="card-title">Projects</h4>
                <p class="card-text">Explore concrete projects in actuarial modeling, machine learning, educational development, and Python applications.</p>
                <a href="projects/index.html" class="btnn">Explore</a>
            </div>
        </div>

        <div class="card">
            <div class="card-body">
                <h4 class="card-title">Get in Touch</h4>
                <p class="card-text">Have an idea, a question, or a potential collaboration? I'm open to connecting.</p>
                <a href="contact/index.html" class="btnn">Contact</a>
            </div>
        </div>
    </div>

.. toctree::
   :maxdepth: 2
   :caption: Navigation

   about/index
   cv/index
   projects/index
   contact/index


