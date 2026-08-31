# Urban Microfarming Automation System
## 5-Month Project Roadmap (Mid-April to Mid-August 2026)
### Goal: Portfolio-Ready Proof of Concept + Becca Aiffel Scholarship Application

---

## **Executive Summary**

**Project Vision:** Design and build an automated urban farming system that combines sprouting, vertical hydroponic gardening, and composting automation — optimized for low-resource environments (small spaces, minimal hardware). The system will demonstrate resource-constrained engineering, mechanical + software integration, and scalability from apartment to community scale.

**Target Outcomes by Mid-August:**
- ✅ Functional prototype: sprouting + garden + composting automation
- ✅ Complete control system (Arduino/ESP32 + sensors + automation logic)
- ✅ 10-12 YouTube videos documenting the build journey
- ✅ GitHub repository with code, CAD files, assembly instructions
- ✅ Technical blog post or white paper on design approach
- ✅ Portfolio case study ready for Becca Aiffel application

---

## **PHASE 1: Planning & Foundation (Mid-April to End of April)**
### Duration: ~3 weeks

### Goals:
- Finalize system design and component selection
- Set up GitHub repo and YouTube channel
- Learn/review key technologies needed
- Build your first prototype concept video

### Deliverables:

#### 1.1 System Design Document
Create a clear specification:
- **Sprouting subsystem:** What will you automate? (moisture, light, temperature, harvesting?)
- **Garden subsystem:** Hydroponic type? (NFT, DWC, ebb & flow?) Size? Plant types?
- **Composting subsystem:** What triggers? (moisture sensors, timer, automated mixing?)
- **Integration:** How do these three work together?

**Action:** Sketch out the design in 1-2 days. Take photos/diagrams.

#### 1.2 Component List & BOM (Bill of Materials)
Research and list everything you need:
- Sensors (moisture, temperature, light, humidity, CO2?)
- Actuators (pumps, motors, fans, solenoids)
- Controller (Arduino Mega? ESP32? Raspberry Pi?)
- Growth medium, seeds, tools
- 3D-printable parts vs. purchased vs. fabricated

**Constraints:** Keep cost reasonable. Use repurposable materials where possible.

**Action:** Create a spreadsheet with part names, costs, suppliers (local + online).

#### 1.3 GitHub Repository Setup
- Create repo: `urban-microfarming-automation`
- README with project vision, goals, timeline
- Folder structure:
  ```
  /hardware (CAD files, PCB designs, BOMs)
  /software (firmware, monitoring app code)
  /documentation (design docs, build guides, analysis)
  /media (photos, videos, diagrams)
  /research (existing solutions, academic papers)
  ```
- Create a Kanban board or Issues list with all tasks

**Action:** Set this up in first week of April. Invite feedback from community.

#### 1.4 YouTube Channel & Content Plan
- Create channel: Something like "Cristopher's Microfarming Lab" or "Urban Farm Automation"
- Write channel description linking to your professional vision
- Plan 10-12 videos over 5 months:
  - Ep 1: Problem statement + design overview
  - Ep 2-3: Component selection & BOM explanation
  - Ep 4-6: Building each subsystem (sprouting, garden, composting)
  - Ep 7-9: Software/automation setup and calibration
  - Ep 10: System integration & first harvest
  - Ep 11-12: Results, lessons learned, next iterations

**Action:** Record Ep 1 by end of April (5-10 min).

#### 1.5 Skill Gaps & Learning Plan
Assess what you need to learn:
- [ ] Hydroponic system design (read 2-3 papers/tutorials)
- [ ] Sensor integration with Arduino/ESP32 (refresh or deepen)
- [ ] PID control loops (for pump/moisture automation)
- [ ] Data logging & visualization (optional but impressive)
- [ ] Basic plant biology (sprouting, germination, nutrient timing)

**Action:** Spend 2-3 hours researching each area. Bookmark resources.

---

## **PHASE 2: Subsystem Design & Prototyping (May)**
### Duration: ~4 weeks

### Goals:
- Design and test each subsystem independently
- Build rough prototypes
- Document everything on YouTube

### Deliverables:

#### 2.1 Sprouting Subsystem (Week 1-2 of May)
**Scope:** Automated sprouting jars or trays with moisture control and light cycles.

**Design Questions:**
- How many sprouts at a time? (e.g., 4-6 mason jars)
- Moisture method: misting, soaking, or drip irrigation?
- Light: LED strip on timer? Controlled by software?
- Automation: solenoid valve for watering, relay for LED?

**Prototype Tasks:**
1. Build mechanical frame for jars (3D print or PVC)
2. Design moisture sensor placement (capacitive soil moisture sensor)
3. Wire solenoid valve + pump for water delivery
4. Set up timer/relay for LED lighting
5. Test with water (no seeds yet) — does water reach all jars evenly?

**Software (Basic):**
- Arduino sketch that reads moisture sensor every 10 min
- If moisture < threshold, activate pump for 5 seconds
- If light timer, turn LED on/off

**YouTube:** Film Ep 2-3 (component overview, mechanical build)

**By End of Week 2:** Working prototype that can water 4-6 sprout containers automatically.

---

#### 2.2 Composting Subsystem (Week 2-3 of May)
**Scope:** Automated composting bin that monitors and mixes waste.

**Design Questions:**
- Size of bin? (10-20L for small apartment)
- What triggers mixing? (timer every 2 days? Or moisture sensor?)
- Mixing mechanism: rotating drum, agitator arm, or manual chute?
- Moisture monitoring: too dry = add water, too wet = add dry material?

**Prototype Tasks:**
1. Build sealed bin frame with motorized agitator (or rotating mechanism)
2. Design moisture sensor probe placement
3. Add small solenoid valve for water misting (if dry)
4. Wire motor + relays to controller

**Software:**
- Read moisture sensor every 6 hours
- If moisture < 40%, activate misting solenoid for 10 sec
- Every 48 hours, activate agitator motor for 30 sec (mixing)
- Log data to SD card

**YouTube:** Film Ep 4 (composting design & build)

**By End of Week 3:** Working compost bin that auto-moisturizes and mixes.

---

#### 2.3 Hydroponic Garden Subsystem (Week 3-4 of May)
**Scope:** Small vertical or tabletop hydroponic system (herbs, leafy greens).

**Design Questions:**
- System type: NFT (nutrient film technique), DWC (deep water culture), or Kratky method?
- Number of plants? (6-12 to start)
- Growth medium: rockwool, clay pellets, or coconut coir?
- Nutrients: liquid solution, periodic testing, or automated dosing?

**Prototype Tasks:**
1. Build growing bed (PVC pipes or 3D-printed channels)
2. Design water pump circulation (timer or continuous?)
3. Install temperature & dissolved oxygen sensors (optional but impressive)
4. Add LED grow lights (with dimming capability?)
5. Design nutrient reservoir (with float sensor to auto-refill)

**Software:**
- Monitor water temperature, pH (if sensor available), nutrient level
- Pump runs on schedule (e.g., 15 min on, 45 min off for NFT)
- LED lights on 16-hour cycle (with optional intensity control)
- Log data for later analysis

**YouTube:** Film Ep 5-6 (hydroponic design & build)

**By End of May:** Three subsystems working independently, documented on YouTube.

---

## **PHASE 3: Integration & Software (June)**
### Duration: ~4 weeks

### Goals:
- Connect all three subsystems to a single controller
- Build a monitoring/control interface
- Test the full system with plants

### Deliverables:

#### 3.1 Master Controller Design
**Architecture:**
- **Hardware:** ESP32 or Arduino Mega as main controller
- **Sensors:** Multiplex all moisture, temperature, light sensors
- **Actuators:** Pump relays, motor relays, solenoid valves
- **Networking:** WiFi (ESP32) to enable remote monitoring

**Subsystem Communication:**
```
[Sensor 1: Sprout moisture] ---|
[Sensor 2: Compost moisture] --| [ESP32] ---> [Control logic] ---> [Relays/Motors]
[Sensor 3: Garden temp]       --| 
[Sensor 4: Reservoir level]  ---|
```

**Action Items:**
1. Wire all sensors to ESP32 (use analog/digital pins efficiently)
2. Design PCB layout (or use breadboard + jumpers for now)
3. Create power supply distribution (assume 12V for pumps/motors, 5V for sensors)
4. Write master firmware that coordinates all subsystems

#### 3.2 Monitoring & Control Interface
**Option A (Simpler):** Web dashboard
- ESP32 hosts a simple web server
- Display sensor readings in real-time
- Manual buttons to trigger pumps, lights, motors
- Built with HTML/CSS/JavaScript (runs on phone/laptop)

**Option B (More Impressive):** Mobile app
- Flutter or React Native app
- Connect to ESP32 via WiFi
- Real-time graphs of soil moisture, temperature, humidity over time
- Manual controls + automatic scheduling interface

**Recommendation for 5-month timeline:** Start with Option A (web dashboard), expand to Option B if time allows.

**YouTube:** Film Ep 7-8 (software architecture, dashboard demo)

#### 3.3 System Integration Testing
**Week 1-2 of June:**
- Upload master firmware to ESP32
- Test each sensor individually (does it read correctly?)
- Test each actuator (does pump turn on? Does motor spin?)
- Test interdependencies (e.g., if sprout moisture low, pump activates automatically)

**Week 3-4 of June:**
- Start with water only (no plants)
- Run for 1-2 weeks to verify automation logic works
- Fix bugs in sensor readings, pump timing, etc.
- Prepare for plant trials

**YouTube:** Film Ep 9 (integration testing, debugging)

#### 3.4 First Plant Trial
**Late June:** Plant seeds and start the system
- Sprouting tray: Start with fast seeds (mung beans, alfalfa, broccoli) — harvest in 5-7 days
- Hydroponic garden: Plant seedlings or fast-growing greens (lettuce, spinach, herbs)
- Composting: Add kitchen scraps, monitor decomposition

**Documentation:** Daily photos/videos of plant growth, sensor readings, any adjustments needed.

**YouTube:** Film Ep 10 (planting, first growth observations)

---

## **PHASE 4: Optimization & Documentation (July)**
### Duration: ~4 weeks

### Goals:
- Fine-tune system parameters based on first trial results
- Optimize for minimal resource use (water, energy)
- Complete all documentation and portfolio materials

### Deliverables:

#### 4.1 System Optimization
**Data Analysis:**
- Review sensor logs from June: What were the patterns?
- Sprouting: Did moisture levels optimize germination rate?
- Garden: Did nutrient levels hold steady? Any algae growth?
- Composting: How quickly did waste decompose?

**Iterations:**
- Adjust pump timing for better water efficiency
- Optimize LED light cycle for faster growth
- Refine composting moisture setpoints
- Reduce power consumption where possible

**Key Metric:** Calculate the "resource efficiency":
- grams of food produced / liters of water used
- grams of food produced / kWh of electricity used
- % waste converted to compost

**YouTube:** Film Ep 11 (optimization process, lessons learned)

#### 4.2 GitHub Documentation
By early July, ensure your GitHub repo is **complete and production-ready:**

**README.md:**
- Clear project description (problem + solution)
- System overview diagram (ASCII art or image)
- Features list
- Bill of materials with links to buy
- Quick-start guide

**/documentation:**
- System design doc (PDF) with diagrams
- Electrical schematics (KiCad or Fritzing)
- Assembly instructions (step-by-step photos)
- Software installation guide
- Troubleshooting guide

**/hardware:**
- All CAD files (STL for 3D printing, DXF for laser cutting)
- PCB layout files (if you designed a custom board)

**/software:**
- Commented, clean firmware code
- Web dashboard code (HTML/CSS/JS)
- README for developers (how to modify, compile, upload)

**/media:**
- Before/after photos of the system
- Time-lapse videos of plant growth
- System architecture diagrams

**Action:** Spend 2 weeks (early July) cleaning up and finalizing these files.

#### 4.3 Technical Blog Post or White Paper
Write a **comprehensive technical article** (2,000-3,000 words) to be published on Medium, Dev.to, or your personal blog. This will be **powerful portfolio material for Becca Aiffel.**

**Outline:**
1. **Introduction:** The problem (urban food insecurity, resource constraints)
2. **Background:** Why automation matters for small-scale farming
3. **System Design:** Architecture, component selection, trade-offs
4. **Implementation:** Hardware build, software stack, integration challenges
5. **Results:** Quantitative data (water saved, food produced, energy used)
6. **Lessons Learned:** What worked, what didn't, what's next
7. **Scalability:** How this design scales to larger spaces or different climates
8. **Conclusion:** Vision for democratizing food production technology

**Tone:** Professional but accessible. Explain technical concepts for both engineers and non-engineers.

**YouTube:** Film Ep 12 (reflect on entire project, share white paper)

#### 4.4 Portfolio Case Study
Create a **1-page visual summary** (infographic-style) of your project:
- Problem statement
- Solution overview (1-2 sentence)
- Key specs (dimensions, sensors, automation points)
- Results (food produced, water saved, etc.)
- Photos of working system
- Links to YouTube/GitHub

This will go on your portfolio/CV for the scholarship.

---

## **PHASE 5: Application Prep & Scholarship Materials (August)**
### Duration: ~4 weeks

### Goals:
- Finalize your Becca Aiffel scholarship application
- Articulate your professional project vision
- Identify target French schools and programs

### Deliverables:

#### 5.1 Scholarship Narrative
Write a **compelling 500-800 word statement** explaining:
- **Your professional vision:** Design resource-constrained systems that democratize access to advanced technology and improve quality of life
- **How this project demonstrates it:** Urban microfarming automation = practical example of mechanical + software + optimization for accessibility
- **Why France:** Which specific schools/programs in France align with your goals? (robotics, embedded systems, sustainable engineering, innovation labs)
- **Your impact goals:** By studying abroad, you want to learn cutting-edge optimization techniques to bring back and scale locally

**Key message:** You're not just a skilled engineer. You're a **systems thinker** committed to **technological equity** and **local problem-solving with global potential.**

#### 5.2 French School & Program Research
Identify **3-5 target institutions** with strong programs in:
- Robotics + embedded systems
- Sustainable engineering
- Systems integration
- Innovation/entrepreneurship labs

**Possible schools** (to research):
- **INSA (Institut National des Sciences Appliquées)** — multiple campuses, strong in robotics, sustainability
- **Grenoble INP** — excellent for systems, automation, robotics
- **École Polytechnique / Télécom Paris** — cutting-edge tech, very competitive
- **Université de Lyon** — good robotics programs
- **IMT Atlantique** — engineering + innovation focus

**For each school, note:**
- Specific master's programs that fit your goals
- Lab/research areas that interest you
- Faculty working in optimization/robotics/sustainability
- Application deadlines
- Becca Aiffel compatibility (does it accept their students?)

#### 5.3 Becca Aiffel Application Package
Compile all materials:
- ✅ Polished CV (updated with Urban Microfarming project)
- ✅ Scholarship narrative (your professional + academic project vision)
- ✅ Project portfolio (GitHub link, YouTube link, case study)
- ✅ Technical white paper or blog post
- ✅ Letters of recommendation (ask professors now; give them detailed brief)
- ✅ Transcripts (ensure good standing in core courses)
- ✅ Proof of French language level (if required)

#### 5.4 Application Timeline
- **Early August:** Finalize narrative, research schools, gather materials
- **Mid-August:** Submit applications to 3-5 target schools
- **August 15:** Becca Aiffel application deadline (verify exact date)
- **Late August:** Polish anything remaining, prepare for interviews

---

## **Parallel Activities: Skills Development**

While building the project, dedicate **2-3 hours per week** to deepening skills for French studies:

### Control Systems & Robotics
- [ ] Work through a PID control tutorial (YouTube: "PID Control for Beginners")
- [ ] Study basic feedback loops in plant growth (soil moisture → water → growth → sensor reading)
- [ ] Read 1-2 papers on automated systems in agriculture

### Embedded Systems & Optimization
- [ ] Deep dive into ESP32 power consumption (sleep modes, efficiency)
- [ ] Learn about edge computing and minimal-resource optimization
- [ ] Code optimization: Can you reduce firmware size? Optimize sensor polling?

### French Language (If Required)
- [ ] If Becca Aiffel requires French proficiency:
  - Dedicate 30-60 min/day to French study (Duolingo, Pimsleur, or formal classes)
  - By August, aim for at least B1 level (intermediate)
  - Practice writing short technical summaries in French

### Open-Source Contribution (Optional but Impressive)
- [ ] Contribute bug fixes or documentation to an existing robotics/farming automation project
- [ ] Shows you're part of a community, not just building solo

---

## **Key Metrics & Success Criteria**

By **Mid-August**, you should have:

### Project Deliverables:
- ✅ Working prototype: sprouting + garden + composting, all automated
- ✅ 12 YouTube videos (one per week)
- ✅ Complete GitHub repo with code, CAD, docs, BOM
- ✅ Technical white paper (2,000+ words) published online
- ✅ Portfolio case study (1-page visual summary)

### Application Readiness:
- ✅ Polished CV highlighting Urban Microfarming project
- ✅ 500-800 word scholarship narrative articulating your professional vision
- ✅ List of 3-5 target French schools with specific programs identified
- ✅ Complete application package ready to submit by mid-August

### Skills & Network:
- ✅ Deepened expertise in control systems, embedded optimization, robotics
- ✅ Growing YouTube community (potential collaborators/followers)
- ✅ Open-source contributions or visible portfolio on GitHub
- ✅ Letters of recommendation from professors (requested, in progress)

---

## **Budget Estimate** (Rough)

| Item | Est. Cost (MXN) | Notes |
|------|-----------------|-------|
| Sensors (moisture, temp, light, pH) | 800-1200 | Can source locally or online |
| Controller (ESP32 or Arduino Mega) | 200-400 | ~$10-20 USD |
| Pumps, motors, solenoids | 600-1000 | Repurpose if possible |
| Growing medium, seeds, nutrients | 400-800 | Depends on scale |
| 3D printing filament | 300-500 | If you have access to printer |
| PVC, wood, misc. materials | 400-700 | Building frame/structure |
| **TOTAL** | **~3,000-5,500 MXN** | (~$150-280 USD) |

*Note: Costs can be significantly reduced by repurposing materials, sourcing locally, and leveraging existing tools/resources.*

---

## **How to Use This Roadmap**

1. **Print or bookmark this document** — refer to it weekly
2. **Break each phase into weekly tasks** — update your calendar in "Dos Gatitos"
3. **Track progress on GitHub Issues** — this keeps you accountable and transparent
4. **Film YouTube episodes on schedule** — consistency matters more than polish
5. **Share progress in your community** — Discord, Reddit, maker spaces — solicit feedback
6. **Adjust as needed** — if something takes longer, shift later phases; the core goal is mid-August readiness

---

## **Final Note**

This project is **not just about building a system.** It's about demonstrating:
- **Systems thinking:** You can design integrated mechanical + software solutions
- **Real-world problem-solving:** You start with a genuine problem, not a theoretical one
- **Resource consciousness:** You optimize for constraints, not abundance
- **Community mindset:** You document and share openly for others to learn/build
- **Scalability vision:** What works in an apartment can scale to a farm, region, country

This narrative is **exactly what Becca Aiffel and French engineering schools want to see** in applicants. Go build it. 🚀

---

**Next Step:** Reply with any questions, or let's create a detailed **monthly calendar** to schedule this into your existing commitments (classes + afternoon work).
