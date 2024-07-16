<h3>Table of Contents</h3>
<ul>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#overview">Overview</a></li>
    <li><a href="#implementation">Implementation</a></li>
    <li><a href="#installation-and-setup">Installation and Setup</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributors">Contributors</a></li>
</ul>

<h3 id="introduction">Introduction</h3>
<div>
   In the rapidly evolving field of robotics, one of the major challenges is enabling robots to efficiently manage multiple tasks simultaneously, a concept we refer to as Simultaneous Work. While humans are adept at using both hands to perform different actions concurrently, robots have yet to achieve comparable proficiency. This project aims to address this gap by leveraging Reinforcement Learning algorithms, exploring their potential to not only match but possibly exceed human capabilities in simultaneous task management. Through this approach, we seek to advance the autonomy and versatility of robotic systems, opening new possibilities for their application in complex, real-world environments.
</div>

<h3 id="overview">Overview</h3>
<div>
   To facilitate this exploration, we leverage <b>Baxter</b>, humanoid robot as our agent. <a href="https://www.ohio.edu/mechanical-faculty/williams/html/pdf/BaxterKinematics.pdf">Baxter</a> is equipped with two highly versatile arms, making it an ideal candidate for studying dual-arm coordination and manipulation tasks. By using state-of-the-art algorithms, we aim to enable Baxter to perform complex, simultaneous operations that require a high degree of dexterity and precision.<br><br>

   <table align="center">
   <tr align="center">
      <td>
         <img width="327" height="300" src="./media/baxter.png">
      </td>
      <td>
         <img width="327" height="300" src="./media/baxter_desc.png">
      </td>
   </tr>
   </table>
   <br>
   The realised environment is fully compatible with the OpenAI Gym framework, allowing for seamless integration with existing RL libraries and tools. The simulation is powered by PyBullet, a robust and widely-used physics engine that provides realistic and accurate modeling of robotic interactions.
   <br>
   <br><img width="800" height="400" src="media/env.png"><br>
</div>

<h3 id="implementation">Implementation</h3>
<div>
   <h4>Project Milestones</h4>
   <ul>
      <li>Creating the environmental setup</li>
      <li>Defining a comprehensive <strong>Joint Reward</strong> function</li>
      <li>Learning simple simultaneous tasks</li>
      <li>Gradually increasing complexity of task</li>
      <li>Elevating interactions</li>
   </ul>

   <p>
      We have developed the environment aimed at facilitating fundamental tasks such as simultaneous lifting, touching, and other coordinated actions. At present, The focus is on formulating the <strong>Markov Decision Process (MDP)</strong> and defining a comprehensive joint reward function.
   </p>

   <p>
      By focusing on these elements, we aim to create a robust framework that will enable the agent to learn and perform simultaneous tasks with increasing complexity. This approach will help in understanding how reinforcement learning algorithms can be utilized to achieve and potentially surpass human-like proficiency in coordinated tasks.
   </p>

   <ol>
      <li>
         <strong>Markov Decision Process (MDP) Formulation</strong>:
         <br><br>
         <div align="center"><img src="https://www.mdpi.com/entropy/entropy-24-00279/article_deploy/html/images/entropy-24-00279-g002.png" width="500"></div>
         <br><br>
         <ul>
            <li>
               <strong>Transition Model</strong>: Establishing the probabilities of transitioning from one state to another given a specific action, which is crucial for predicting the outcomes of the agent's actions.
            </li>
            <li>
               <strong>State Space</strong>: Defining the set of all possible states the agent can be in, considering factors such as the position of its arms, the objects in the environment, and the agent's current task status.
            </li>
            <li>
               <strong>Action Space</strong>: Specifying the set of all possible actions the agent can take in each state, including movements of the arms, grasping, and releasing objects.
            </li>
         </ul>
      </li>
      <li>
         <strong>Joint Reward Function</strong>:
         <br><br>
         <ul>
            <li>
               <strong>Reward Components</strong>: Creating a reward structure that incentivizes successful completion of tasks, efficient use of both arms, and adherence to predefined task constraints and objectives.
            </li>
            <li>
               <strong>Optimization</strong>: Ensuring that the reward function balances immediate rewards for task completion and long-term rewards for developing efficient and effective strategies.
            </li>
         </ul>
      </li>
   </ol>
</div>

<h3 id="installation-and-setup">Installation and Setup</h3>
<blockquote>
   It is recommended to set up a virtual environment to avoid conflicts between package versions installed on your system and keep your workspace organized. To create a virtual environment and activate it, please follow the instructions detailed on <a href="https://docs.python.org/3/library/venv.html">python venv page</a>. The procedure to deactivate the environment is also provided here.
</blockquote>
<br>
<ul>
   <li>Clone the git repo using <code>git clone https://github.com/asood-life/baxter-sma.git</code></li>
   <li>Install the required packages using <code>pip install -e baxter-env</code></li>
</ul>

<h3 id="usage">Usage</h3>
<div>
   After setting up the environment, import it into your workspace using the following python code
</div>
<br>

``` python
import baxter_env
import gym

env = gym.make('baxter_env-v0')
```

<p>
   Once you have imported the environment, you gain access to various functions tailored for different tasks. Here are some of the essential functions along with their descriptions:
</p>

<ul>
   <li>
      <code>env.getImage()</code>: returns a tuple containing a <b>128x128 RGB</b> image along with the depth map of the environment.
   </li>
   <br>
   <p align="center">
      <img src="media/image_data.png" alt="Image Data" width="350">
      <img src="media/depth_data.png" alt="Depth Data" width="350">
      <p align="center"><b>Image Data with Depth Map</b></p>
   </p>
   <li><code>env.moveVC()</code>: moves the joints to a specified position by taking the index of that joint.</li>
   <li><code>env.step()</code>: input a list of actions and perform those while providing the required information about the states.</li>
   <li><code>env.render()</code>: renders the eye view image of the environment.</li>
   <li><code>env.reset()</code>: reset the entire environment and retrieve information regarding the state.</li>
</ul>

<p>In addition to these core functions, we have also implemented some auxiliary functions for specific purposes:</p>

<ul>
   <li><code>env.BeizerCurve()</code>: An implementation of a family of curves that provides a trajectory passing through some points based on specific weights.</li>
   <li><code>env.getReward()</code>: returns the reward for attempting simultaneous touching (a naive implementation).</li>
</ul>
<p>
   For further details on theze functions and their arguments, please refer to the documentation <a href="baxter-env/baxter_env/envs/baxter_env.py">here</a>.
</p>
<p>Example scripts demonstrating the usage of these functions can be found <a href="examples/">here</a>.</p>

<h3 id="contributors">Contributors</h3>
<div>
    <table>
      <td align="center">
         <a href="https://github.com/monako2001">
            <img src="https://avatars2.githubusercontent.com/u/56964886?s=400&v=4" width="100px;" alt=""/>
            <br />
            <sub>
               <b>Mainak Samanta</b>
            </sub>
         </a>
         <br />
      </td>
      <td align="center">
         <a href="https://github.com/asood-life">
            <img src="https://avatars.githubusercontent.com/u/148894491?v=4" width="100px;" alt=""/>
            <br />
            <sub>
               <b>Akshat Sood</b>
            </sub>
         </a>
         <br />
      </td>
      <td align="center">
         <a href="https://github.com/Amshra267">
            <img src="https://avatars1.githubusercontent.com/u/60649720?s=460&u=9ea334300de5e3e7586af294904f4f76c24f5424&v=4" width="100px;" alt=""/>
            <br />
            <sub>
               <b>Aman Mishra</b>
            </sub>
         </a>
         <br />
      </td>
      <td align="center">
         <a href="https://github.com/arch-raven">
            <img src="https://avatars1.githubusercontent.com/u/55887731?s=400&u=7e70757a37e409360fda094f1f61fa1f261f8111&v=4" width="100px;" alt=""/>
            <br />
            <sub>
               <b>Aditya Kumar</b>
            </sub>
         </a>
         <br />
      </td>
   </table>
</div>

<hr>
<div>
    Thank you for visiting! If you find value in this project, please consider giving it a ⭐ star. Your support is greatly appreciated and assists others discover the project. If you have any requests for enhancements or find any bugs, please report them under <a href="https://github.com/asood-life/baxter-sma/issues">Issues</a>. Your feedback is invaluable in making this project better for everyone.
</div>
