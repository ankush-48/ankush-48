## About Me

🚀 **AI Engineer | Software Developer | Full-Stack Enthusiast | Problem Solver**

💡 Passionate about building intelligent systems that combine **AI, LLMs, RAG, Agentic AI, Machine Learning, Cloud, and Full-Stack Development** to solve real-world problems.

<p align="center">
  <img alt="Coding animation" width="320" src="https://media.giphy.com/media/ZVik7pBtu9dNS/giphy.gif" />
</p>

### 🔭 Currently Building
✨ AI Agents • 🤖 LLM Applications • 🧠 RAG Pipelines • 🌐 Full-Stack AI Products • ⚡ Intelligent Automation

### 🌱 Currently Learning
📚 Multi-Agent AI • 🕸️ LangGraph • ☸️ Kubernetes • 🚀 MLOps • ☁️ AWS & GCP • 🔄 CI/CD • 🗄️ Vector Databases • 🧩 Prompt Engineering

### 👯 Open to Collaborate On
🤝 AI/ML • LLM Applications • Open Source • Full-Stack Projects • Computer Vision • Data Science • Agentic AI

### 💬 Ask Me About
🐍 Python • ☕ Java • 🔗 LangChain • 🕸️ LangGraph • 📦 FastAPI • 🐳 Docker • ☁️ AWS • 🗄️ SQL • 🧠 TensorFlow • 📊 Data Analytics • 🤖 AI Agents

### 🎯 Current Goal
Building production-ready AI applications that are scalable, reliable, and solve meaningful real-world problems.

### ⚡ Fun Fact
💙 I genuinely enjoy learning new technologies, experimenting with AI frameworks, and turning ideas into working products faster than I can write them down. 🚀✨

---

> 🌟 **"Code. Learn. Build. Repeat. Every project is another step toward creating technology that makes a difference."**

<div align="center">

**🚀 "Great software isn't built by writing more code. It's built by solving the right problems."**

💡 Learn relentlessly. Build fearlessly. Ship consistently.

⭐ *"The best way to predict the future is to build it."*

</div>

## Flagship

<div align="center"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/section-01.svg" width="100%" alt="Flagship"/></div>

### Relay · Offline-First Payment Network Simulator

<a href="https://relay-offline-payment-demo.onrender.com/"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/flagship-relay.svg?v=2" width="100%" alt="Relay payment flow from offline queue through encrypted mesh to the simulated ledger"/></a>

*Java 17 · Spring Boot · JavaScript · H2 · IndexedDB*

Built a UPI-style payment simulator that queues transfers offline and syncs them on reconnect. Used AES-GCM and RSA-OAEP to encrypt payment packets, plus idempotency keys, freshness checks, and transactional ledger updates to handle duplicate and concurrent arrivals.

<a href="https://relay-offline-payment-demo.onrender.com/">Live demo</a> · <a href="https://github.com/ankush-48/relay-offline-payment-demo">Source code</a>

#### Architecture and payment flow

<img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/relay-architecture.svg" width="100%" alt="Animated architecture diagram: browser queue, Spring Boot encryption, virtual peer mesh, bridge validation, and H2 ledger settlement"/>

1. **Queue locally.** The browser saves a payment request in IndexedDB, with a localStorage fallback. The request waits for connectivity and an active demo session.
2. **Seal and forward.** The server encrypts the payload with AES-GCM, wraps the key with RSA-OAEP, and sends the envelope through the simulated peer mesh.
3. **Validate at the bridge.** The bridge decrypts the request, checks freshness and idempotency, and attempts settlement. A transient sync failure leaves the request available for retry.
4. **Confirm at the ledger.** The simulated ledger validates balances and updates them in a transaction. The UI shows confirmation after a settled response.

<img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/relay-states.svg" width="100%" alt="State diagram: queued, syncing, validating, and confirmed only after settlement"/>

#### Try it live

[Open guest sandbox](https://relay-offline-payment-demo.onrender.com/) · [Dashboard and cashflow](https://relay-offline-payment-demo.onrender.com/#/dashboard) · [Send a simulated payment](https://relay-offline-payment-demo.onrender.com/#/dashboard/send) · [Live network monitor](https://relay-offline-payment-demo.onrender.com/#/dashboard/system)

Enter **Guest access** first. In the network monitor, use **Refresh telemetry** to inspect API response time, mesh nodes and the local queue. The dashboard shows simulated cashflow and ledger activity after settlement.

#### Relay in action

<div align="center">
<a href="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/projects/relay-home.png"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/projects/relay-home.png" width="49%" alt="Relay landing page"/></a> <a href="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/projects/relay-lifecycle.png"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/projects/relay-lifecycle.png" width="49%" alt="Offline payment request lifecycle"/></a>
<br/>
<a href="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/projects/relay-dashboard.png"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/projects/relay-dashboard.png" width="49%" alt="Guest dashboard and simulated ledger"/></a> <a href="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/projects/relay-send.png"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/projects/relay-send.png" width="49%" alt="Simulated payment form"/></a>
<br/>
<a href="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/projects/relay-receive.png"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/projects/relay-receive.png" width="49%" alt="Demo payment identifier"/></a> <a href="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/projects/relay-scan.png"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/projects/relay-scan.png" width="49%" alt="Scan and pay demo with manual recipient lookup"/></a>
<br/>
<a href="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/projects/relay-network.png"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/projects/relay-network.png" width="49%" alt="Network monitor and simulated mesh topology"/></a>
</div>

## Selected Work

<table>
<tr>
<td width="50%" valign="top">
<a href="https://k7v3m9q2-five.vercel.app"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/project-wind-preview.svg" width="100%" alt="Wind Vintage, UK wind forecast accuracy dashboard. Screenshot shows actual versus forecast generation. Analyzed 20,700+ records with forecast error, bias, and coverage metrics."/></a><br/>
<a href="https://k7v3m9q2-five.vercel.app">Live dashboard</a> · <a href="https://github.com/ankush-48/k7v3m9q2">Code</a>
</td>
<td width="50%" valign="top">
<a href="https://github.com/ankush-48/AI-Multi-Agent-Social-Debate-System"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/project-debate.svg" width="100%" alt="Multi-Agent Debate — An LLM debate system with memory. Debate prompt, then LangGraph routing, then FAISS-backed memory. 5+ LLM personas."/></a><br/>
<a href="https://github.com/ankush-48/AI-Multi-Agent-Social-Debate-System">Code</a>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/ankush-48/ai-project-health-reporting-agent"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/project-analytics.svg" width="100%" alt="Enterprise RAG — Structured project health analytics. Project records, then Retrieval + LLM, then Pydantic validation. 50+ profiles processed concurrently."/></a><br/>
<a href="https://github.com/ankush-48/ai-project-health-reporting-agent">Code</a>
</td>
<td width="50%" valign="top">
<a href="https://github.com/ankush-48/Containerized-Flask-REST-API-with-Kubernetes-MongoDB"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/project-eks.svg" width="100%" alt="Flask on AWS EKS — Containerized API with persistent storage. HTTP requests, then Flask replicas, then MongoDB + EBS. Autoscaling from 2 to 5 pods."/></a><br/>
<a href="https://github.com/ankush-48/Containerized-Flask-REST-API-with-Kubernetes-MongoDB">Code</a>
</td>
</tr>
<tr>
<td colspan="2" align="center">
<a href="https://github.com/ankush-48/Fear-Greed-vs-Profit-A-Behavioral-Analysis-of-Crypto-Trading"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/project-sentiment.svg" width="50%" alt="Fear &amp; Greed vs. Profit — Crypto trading across sentiment regimes. Hyperliquid trades, then Sentiment index, then PnL comparison. 480 days of trading data."/></a><br/>
<a href="https://github.com/ankush-48/Fear-Greed-vs-Profit-A-Behavioral-Analysis-of-Crypto-Trading">Code</a>
</td>
</tr>
</table>

## Achievements

<div align="center"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/section-03.svg" width="100%" alt="Achievements"/></div>

- **CICADA 2023 Hackathon** · Led a four-person team through a 24-hour build at Atria Institute of Technology.
- **CodeChef Silver Problem Solver** · Solved 270+ data structures and algorithms problems in Java and Python.
- **Presidency University Innovation Expo** · Selected among the top 70 of 450 teams in May 2023.

[CodeChef](https://www.codechef.com/users/ankush48) · [LeetCode](https://leetcode.com/u/Ankush48/)

## Experience

<div align="center"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/section-04.svg" width="100%" alt="Experience"/></div>

### Mphasis Ltd · Associate Software Engineer Intern

*Feb 2026 – Apr 2026 · Bengaluru, India*

- Built 12+ REST endpoints with Java and Spring Boot, with sub-200 ms response times in concurrent request benchmarks.
- Reduced database response times by 20% across 15+ relational tables by optimizing MySQL queries and tuning Hibernate mappings.
- Improved page-load speed by 25% across 10+ responsive frontend modules built with HTML, CSS, Bootstrap, and TypeScript.

### Evoastra Ventures · Data Science Intern, Data &amp; Pipelines

*Jul 2025 – Aug 2025 · Remote*

- Automated daily data collection with BeautifulSoup and Selenium, processing 50,000+ data points and saving 15+ hours of manual research per week.
- Built a DenseNet201 CNN–LSTM image captioning model and served it through Flask.
- Improved inference speed by 30% in benchmarks through tuning, custom tokenization, and optimized feature extraction.

## Live from GitHub

<a href="https://github.com/ankush-48#contributions-calendar"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/github/contribution-heatmap.svg" width="100%" alt="GitHub contribution heatmap and statistics for Ankush Yadav"/></a>

## Education

**Presidency University**, Bengaluru  
B.Tech in Computer Science and Engineering · Dec 2022 – Nov 2026 · CGPA 7.7/10

## Certifications &amp; Training

- **AWS** · AWS Certified Cloud Practitioner
- **Google Cloud** · GenAI Studio
- **Microsoft** · Azure Essentials, Azure AI Essentials, Career Essentials in Software Development, and Career Essentials in Data Analysis
- **HP** · HP Data Analytics
- **Cisco** · Networking Basics

## Tech Stack

- **LLMs & agents** · LangChain, LangGraph, RAG, FAISS, Sentence-Transformers, Groq, and Llama 3.3.
- **Software & infrastructure** · Spring Boot, Hibernate, REST APIs, Docker Compose, AWS EKS, and SQL.
- **Data & ML** · Exploratory data analysis, feature engineering, statistical modeling, CNNs, LSTMs, Tableau, and Seaborn.

### Languages & Markup

![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![LaTeX](https://img.shields.io/badge/latex-%23008080.svg?style=for-the-badge&logo=latex&logoColor=white)
![PHP](https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![R](https://img.shields.io/badge/r-%23276DC3.svg?style=for-the-badge&logo=r&logoColor=white)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)

### Cloud & Hosting

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Vercel](https://img.shields.io/badge/vercel-%23000000.svg?style=for-the-badge&logo=vercel&logoColor=white)
![Netlify](https://img.shields.io/badge/netlify-%23000000.svg?style=for-the-badge&logo=netlify&logoColor=%2300C7B7)
![Firebase](https://img.shields.io/badge/firebase-%23039BE5.svg?style=for-the-badge&logo=firebase)
![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white)

### Web, Mobile & Backend

![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Flutter](https://img.shields.io/badge/Flutter-%2302569B.svg?style=for-the-badge&logo=Flutter&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Express.js](https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB)
![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![Next JS](https://img.shields.io/badge/Next-black?style=for-the-badge&logo=next.js&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![React Native](https://img.shields.io/badge/react_native-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![React Query](https://img.shields.io/badge/-React%20Query-FF4154?style=for-the-badge&logo=react%20query&logoColor=white)
![Spring](https://img.shields.io/badge/spring-%236DB33F.svg?style=for-the-badge&logo=spring&logoColor=white)
![Three js](https://img.shields.io/badge/threejs-black?style=for-the-badge&logo=three.js&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Apache Tomcat](https://img.shields.io/badge/apache%20tomcat-%23F8DC75.svg?style=for-the-badge&logo=apache-tomcat&logoColor=black)

### Databases & Data Platforms

![AmazonDynamoDB](https://img.shields.io/badge/Amazon%20DynamoDB-4053D6?style=for-the-badge&logo=Amazon%20DynamoDB&logoColor=white)
![Firebase](https://img.shields.io/badge/firebase-a08021?style=for-the-badge&logo=firebase&logoColor=ffcd34)
![MicrosoftSQLServer](https://img.shields.io/badge/Microsoft%20SQL%20Server-CC2927?style=for-the-badge&logo=microsoft%20sql%20server&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)

### AI, Data Science & Analytics

![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![mlflow](https://img.shields.io/badge/mlflow-%23d9ead3.svg?style=for-the-badge&logo=numpy&logoColor=blue)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Scipy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![Power Bi](https://img.shields.io/badge/power_bi-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

### Design & Graphics

![OpenGL](https://img.shields.io/badge/OpenGL-%23FFFFFF.svg?style=for-the-badge&logo=opengl)
![Adobe](https://img.shields.io/badge/adobe-%23FF0000.svg?style=for-the-badge&logo=adobe&logoColor=white)
![Adobe After Effects](https://img.shields.io/badge/Adobe%20After%20Effects-9999FF.svg?style=for-the-badge&logo=Adobe%20After%20Effects&logoColor=white)
![Adobe Photoshop](https://img.shields.io/badge/adobe%20photoshop-%2331A8FF.svg?style=for-the-badge&logo=adobe%20photoshop&logoColor=white)
![Blender](https://img.shields.io/badge/blender-%23F5792A.svg?style=for-the-badge&logo=blender&logoColor=white)
![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white)

### Developer Tools, Testing & Infrastructure

![Windows Terminal](https://img.shields.io/badge/Windows%20Terminal-%234D4D4D.svg?style=for-the-badge&logo=windows-terminal&logoColor=white)
![Apache Maven](https://img.shields.io/badge/Apache%20Maven-C71A36?style=for-the-badge&logo=Apache%20Maven&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Jest](https://img.shields.io/badge/-jest-%23C21325?style=for-the-badge&logo=jest&logoColor=white)
![Selenium](https://img.shields.io/badge/-selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)
![Cisco](https://img.shields.io/badge/cisco-%23049fd9.svg?style=for-the-badge&logo=cisco&logoColor=black)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

## More GitHub Stats

<table>
<tr><td width="50%"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/github/account-stats.svg" alt="GitHub account statistics" width="100%"/></td><td width="50%"><a href="https://github.com/ankush-48#contributions-calendar">View GitHub’s contribution calendar</a></td></tr>
<tr><td width="50%"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/github/top-languages.svg" alt="Top languages" width="100%"/></td><td width="50%"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/github/profile-details.svg" alt="Profile details" width="100%"/></td></tr>
<tr><td width="50%"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/github/summary-stats.svg" alt="Profile summary statistics" width="100%"/></td><td width="50%"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/github/activity-by-hour.svg" alt="Commit activity by hour, UTC+5:30" width="100%"/></td></tr>
<tr><td width="50%"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/github/repos-per-language.svg" alt="Repositories per language" width="100%"/></td><td width="50%"><img src="https://raw.githubusercontent.com/ankush-48/ankush-48/main/assets/github/commits-per-language.svg" alt="Commits per language" width="100%"/></td></tr>
</table>

Charts refresh on a daily schedule. Each chart keeps its last successful copy if its provider is unavailable.

<div align="center">

<a href="https://ankush-yadav.netlify.app/">Portfolio</a> · <a href="https://linkedin.com/in/ankush-yadav48">LinkedIn</a> · <a href="mailto:ay3068756@gmail.com">Email</a>

</div>
