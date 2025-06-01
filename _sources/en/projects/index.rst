.. _projects-index:

Projects
===========

.. raw:: html

    <style>
        .jumbotron {
            background: linear-gradient(135deg, #2c3e50, #4ca1af);
            color: white;
            text-align: center;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
            word-wrap: break-word;
        }
        .section {
            font-weight: bold;
            text-align: center;
            margin: 2rem 0 1rem;
            font-size: 2rem;
            color: #333;
        }
        .card {
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
            padding: 1.5rem;
            background-color: #f9f9f9;
            border-left: 5px solid #4ca1af;
            position: relative;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        .card:hover {
            transform: scale(1.03);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        .card h2 {
            margin-top: 0;
            color: #4ca1af;
        }
        .mini-card {
            background-color: #fff;
            border-radius: 10px;
            padding: 1rem;
            margin-top: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        .mini-card ul {
            padding-left: 20px;
            margin: 0.5rem 0;
        }
        .mini-card ul li {
            margin-bottom: 5px;
        }
        .logosec {
            width: 50px;
            height: 50px;
            position: absolute;
            top: 10px;
            right: 10px;
        }
        .btn-primary {
            background-color: #4ca1af;
            border: none;
            padding: 0.5rem 1rem;
            color: white;
            border-radius: 5px;
            text-decoration: none;
        }
        .btn-primary:hover {
            background-color: #3b8a9e;
        }
    </style>

    <div class="jumbotron">
        <h1 class="display-4">Completed Projects</h1>
        <p>Real-world applications in actuarial science, data science, and applied statistics</p>
    </div>

    <div class="section">Shiny Applications</div>

    <div class="card">
        <h2>Car Claim Prediction</h2>
        <div class="mini-card">
            <ul>
                <li>Interactive exploration of variables (driver age, vehicle power...)</li>
                <li>GLM and GAM modeling</li>
                <li>Dynamic visualizations (Leaflet, correlations)</li>
                <li>Model evaluation: AIC, BIC, MAE, ROC</li>
                <li>Claim frequency prediction</li>
            </ul>
            <a href="https://johngab7.shinyapps.io/PredictCarCrash/" target="_blank" class="btn-primary">Open App</a>
        </div>
        <img src="../../../../_static/log.png" alt="Insurance Analytics Logo" class="logosec">
    </div>

    <div class="card">
        <h2>Mortality Rate Analysis</h2>
        <div class="mini-card">
            <ul>
                <li>Country selection and download from HMD database</li>
                <li>Missing value detection</li>
                <li>Visualization and projection using Lee-Carter</li>
                <li>Custom life table export</li>
            </ul>
            <a href="https://johngab7.shinyapps.io/MortalityApp/" target="_blank" class="btn-primary">Open App</a>
        </div>
    </div>

    <div class="card">
        <h2>MLE Convergence</h2>
        <div class="mini-card">
            <p>Visualize convergence paths, estimated parameters, and performance for different models and scenarios.</p>
            <a href="https://johngab7.shinyapps.io/mle_convergence_in_r/" target="_blank" class="btn-primary">Open App</a>
        </div>
    </div>

    <div class="card">
        <h2>Monte Carlo GMM Estimation</h2>
        <div class="mini-card">
            <p>Simulate processes to understand GMM convergence under various contexts and sample sizes.</p>
            <a href="https://johngab7.shinyapps.io/monte_carlo_for_gmm_estimation/" target="_blank" class="btn-primary">Open App</a>
        </div>
    </div>

    <div class="section">Educational Projects</div>

    <div class="card">
        <h2>Actu-Basics</h2>
        <div class="mini-card">
            <p>Learning platform to master the basics of actuarial science, statistics and data analysis. Visual teaching meets serious modeling.</p>
            <a href="https://johngab7.github.io/Actu_Basics/" target="_blank" class="btn-primary">Explore Actu-Basics</a>
        </div>
        <img src="../../../../_static/log.png" alt="Actu-Basics Logo" class="logosec">
    </div>
