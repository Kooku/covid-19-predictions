import matplotlib.pyplot as plt

x_coordinates = []
stay_home_ranks = []
social_distancing_ranks = []
coronavirus_lockdown_ranks = []
stay_safe_ranks = []
fake_news_ranks = []
contact_tracing_ranks = []
herd_immunity_ranks = []
spread_coronavirus_ranks = []
public_health_ranks = []

day_from_march_22nd = 1
for i in range(22, 32):
    f = open("2020-03-"+ str(i) +"_top1000bigrams.csv", "r")
    rank_count = 1
    
    x_coordinates.append(day_from_march_22nd)
    day_from_march_22nd += 1

    for line in f:
        arr = line.split(",")
       
        if arr[0] == "gram":
            continue

        if arr[0] == "stay home":
            stay_home_ranks.append(rank_count)
        elif arr[0] == "social distancing":
            social_distancing_ranks.append(rank_count)
        elif arr[0] == "coronavirus lockdown":
            coronavirus_lockdown_ranks.append(rank_count)
        elif arr[0] == "stay safe":
            stay_safe_ranks.append(rank_count)
        elif arr[0] == "fake news":
            fake_news_ranks.append(rank_count)
        elif arr[0] == "contact tracing":
            contact_tracing_ranks.append(rank_count)
        elif arr[0] == "herd immunity":
            herd_immunity_ranks.append(rank_count)
        elif arr[0] == "spread coronavirus":
            spread_coronavirus_ranks.append(rank_count)
        elif arr[0] == "public health":
            public_health_ranks.append(rank_count)


        rank_count += 1

for i in range(1, 16):
    i_str = "0" + str(i) if i < 10 else str(i)
    f = open("2020-04-"+ i_str +"_top1000bigrams.csv", "r")
    rank_count = 1

    x_coordinates.append(day_from_march_22nd)
    day_from_march_22nd += 1
    
    for line in f:
        arr = line.split(",")
        
        if arr[0] == "gram":
            continue

        if arr[0] == "stay home":
            stay_home_ranks.append(rank_count)
        elif arr[0] == "social distancing":
            social_distancing_ranks.append(rank_count)
        elif arr[0] == "coronavirus lockdown":
            coronavirus_lockdown_ranks.append(rank_count)
        elif arr[0] == "stay safe":
            stay_safe_ranks.append(rank_count)
        elif arr[0] == "fake news":
            fake_news_ranks.append(rank_count)
        elif arr[0] == "contact tracing":
            contact_tracing_ranks.append(rank_count)
        elif arr[0] == "herd immunity":
            herd_immunity_ranks.append(rank_count)
        elif arr[0] == "spread coronavirus":
            spread_coronavirus_ranks.append(rank_count)
        elif arr[0] == "public health":
            public_health_ranks.append(rank_count)

        rank_count += 1

plt.plot(x_coordinates, stay_home_ranks, label = "Stay Home")
plt.plot(x_coordinates, social_distancing_ranks, label = "Social Distancing")
plt.plot(x_coordinates, coronavirus_lockdown_ranks, label = "Coronavirus Lockdown")
plt.plot(x_coordinates, stay_safe_ranks, label = "Stay Safe")
plt.plot(x_coordinates, fake_news_ranks, label = "Fake News")
# plt.plot(x_coordinates, contact_tracing_ranks, label = "Contact Tracing")
# plt.plot(x_coordinates, herd_immunity_ranks, label = "Herd Immunity")
plt.plot(x_coordinates, spread_coronavirus_ranks, label = "Spread Coronavirus")
plt.plot(x_coordinates, public_health_ranks, label = "Public Health")

plt.legend()
plt.xlabel('x Days from March 21st')
plt.ylabel('Bigram Ranking')

plt.show()
