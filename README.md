# Demonstration Location Notification Service (Team: Seewith)

## Propose
- We want to give people a heads-up on the real-time location and time of the demonstration.
- It is intended to reduce transportation inconvenience for ordinary citizens.
- It seeks to reduce the risk to ordinary citizens.

## Method
- Collect the protest schedule at the Seoul Metropolitan Police Agency. (https://www.smpa.go.kr/user/nd54882.do)
- Because it is a pdf file, pdf scan(crawling) and text extraction(PyPDF2)

<img width="525" alt="pdf scan" src="https://user-images.githubusercontent.com/63955072/122699350-31537080-d284-11eb-8f0e-e3ce1a9fe510.PNG">

- Extract Latitude Hardness to Address Using API (seewith.ipynb)
> Data collected by pdf file

<img width="288" alt="location 1" src="https://user-images.githubusercontent.com/63955072/122700221-d28ef680-d285-11eb-8967-f97d1ece9655.PNG">

> Build with kakao API

<img width="627" alt="location 2" src="https://user-images.githubusercontent.com/63955072/122700474-4f21d500-d286-11eb-9301-ed8212ad650b.PNG">

> Latitude Hardness Extraction

<img width="309" alt="location 3" src="https://user-images.githubusercontent.com/63955072/122700576-86908180-d286-11eb-8c71-3527996ef910.PNG">

> Extract Latitude Hardness to Address

<img width="397" alt="location 4" src="https://user-images.githubusercontent.com/63955072/122700648-a45de680-d286-11eb-837a-750ac66454f4.PNG">

## Output
- Map Visualization (seewith2.ipynb)

> Visualization 1

<img width="552" alt="location 5" src="https://user-images.githubusercontent.com/63955072/122700695-b9d31080-d286-11eb-9efd-f96d78b4f7d2.PNG">

> Visualization 2 (Markdown)

<img width="490" alt="location 6" src="https://user-images.githubusercontent.com/63955072/122700792-e9821880-d286-11eb-8732-6a2cb1228bc6.PNG">

## Conclusion
- Visualizations were drawn based on the scale of the demonstration.
- The location of the demonstrations was more specific.
- The location and scale of daily demonstrations can be schematically plotted on Seoul maps in real time.
