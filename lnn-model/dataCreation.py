import pandas as pd

# Sample dataset
data = [
    {
        "Input Text": "I am a 45-year-old female with breast cancer, experiencing a dull ache in my left shoulder for the past week. I feel frustrated because the pain interferes with my daily activities. Despite taking my prescribed pain medication, it hasn’t alleviated the discomfort.",
        "Cleaned Text": "dull ache left shoulder past week feel frustrated pain interfere daily activity prescribed pain medication alleviate discomfort",
        "Pain Intensity": "Moderate",
        "Pain Type": "Dull ache",
        "Body Part": "Left shoulder",
        "Duration": "For the past week",
        "Sentiment": "Frustrated"
    },
    {
        "Input Text": "As a 60-year-old male undergoing chemotherapy for lung cancer, I have been experiencing severe chest pain that feels sharp and debilitating. It started two days ago and has made it hard for me to breathe deeply. I’ve been using heat packs, but they don’t seem to help much. This situation makes me anxious about my health.",
        "Cleaned Text": "severe chest pain sharp debilitating start two days hard breathe deep heat packs help much anxious health",
        "Pain Intensity": "Severe",
        "Pain Type": "Sharp",
        "Body Part": "Chest",
        "Duration": "Started two days ago",
        "Sentiment": "Anxious"
    },
    {
        "Input Text": "I am a 54-year-old Caucasian female with breast cancer who has been experiencing severe pain in my right shoulder. The pain started three days ago and feels like a deep ache that radiates down my arm. I’ve tried over-the-counter painkillers, but they haven’t helped. This pain is affecting my daily activities, and I am concerned about its progression.",
        "Cleaned Text": "54-year-old Caucasian female breast cancer severe pain right shoulder deep ache radiate down arm tried over-the-counter painkillers not help affecting daily activities concerned progression",
        "Pain Intensity": "Severe",
        "Pain Type": "deep ache",
        "Body Part": "right shoulder",
        "Duration": "three days",
        "Sentiment": "Negative"
    },
    {
        "Input Text": "I am a 45-year-old Hispanic male diagnosed with lung cancer. For the past week, I have experienced a dull ache in my chest that worsens when I cough. While it's uncomfortable, I remain optimistic about my treatment. I am currently managing it with prescribed medication.",
        "Cleaned Text": "45-year-old Hispanic male lung cancer dull ache chest worsen cough uncomfortable optimistic treatment managing prescribed medication",
        "Pain Intensity": "Moderate",
        "Pain Type": "dull ache",
        "Body Part": "chest",
        "Duration": "for the past week",
        "Sentiment": "Positive"
    },
    {
        "Input Text": "I am a 32-year-old Black female with ovarian cancer, experiencing severe cramping in my lower abdomen for the last four days. The pain is debilitating, and it feels like a constant tightening. I've tried hot packs, but they only provide temporary relief. This pain makes it hard to focus on anything else.",
        "Cleaned Text": "32-year-old Black female ovarian cancer severe cramping lower abdomen last four days debilitating constant tightening tried hot packs only temporary relief hard focus anything else",
        "Pain Intensity": "Severe",
        "Pain Type": "cramping",
        "Body Part": "lower abdomen",
        "Duration": "for the last four days",
        "Sentiment": "Negative"
    },
    {
        "Input Text": "I am a 60-year-old Asian male with prostate cancer who feels occasional sharp pains in my lower back. This has been happening for about a week. I try to stay active, and despite the pain, I remain hopeful about my treatment plan. However, it can be frustrating when the pain interrupts my daily routine.",
        "Cleaned Text": "60-year-old Asian male prostate cancer occasional sharp pains lower back about a week try stay active remain hopeful treatment plan frustrating pain interrupt daily routine",
        "Pain Intensity": "Moderate",
        "Pain Type": "sharp",
        "Body Part": "lower back",
        "Duration": "about a week",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "As a 38-year-old White female with cervical cancer, I have a continuous burning sensation in my pelvis that started two weeks ago. It is quite intense, and I have not found anything that alleviates it. This pain is impacting my emotional well-being, and I feel anxious about my condition.",
        "Cleaned Text": "38-year-old White female cervical cancer continuous burning sensation pelvis started two weeks ago intense not find anything alleviate impacting emotional well-being anxious condition",
        "Pain Intensity": "Severe",
        "Pain Type": "burning",
        "Body Part": "pelvis",
        "Duration": "two weeks",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 29-year-old Black male diagnosed with leukemia who has been feeling mild headaches for the past month. While the headaches are not severe, they are persistent. I am trying to manage my symptoms with hydration and rest, which seems to help a little.",
        "Cleaned Text": "29-year-old Black male leukemia mild headaches past month not severe persistent trying manage symptoms hydration rest help little",
        "Pain Intensity": "Mild",
        "Pain Type": "headaches",
        "Body Part": "head",
        "Duration": "for the past month",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 47-year-old Hispanic female with colorectal cancer experiencing severe pain in my abdomen that started after my last chemotherapy session. It feels like a stabbing sensation and makes it hard to eat or even move. I have discussed this with my doctor, but the pain continues.",
        "Cleaned Text": "47-year-old Hispanic female colorectal cancer severe pain abdomen start after last chemotherapy session stabbing sensation hard eat move discussed doctor pain continues",
        "Pain Intensity": "Severe",
        "Pain Type": "stabbing",
        "Body Part": "abdomen",
        "Duration": "after last chemotherapy session",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "As a 50-year-old Caucasian male with bladder cancer, I sometimes experience a mild, nagging pain in my lower abdomen. It tends to come and go, but it doesn’t stop me from enjoying life. I remain positive and focus on the good things.",
        "Cleaned Text": "50-year-old Caucasian male bladder cancer sometimes experience mild nagging pain lower abdomen come go doesn’t stop enjoying life remain positive focus good things",
        "Pain Intensity": "Mild",
        "Pain Type": "nagging",
        "Body Part": "lower abdomen",
        "Duration": "sometimes",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 31-year-old Asian female with multiple myeloma experiencing severe pain in my back and legs. This pain started a week ago and has been worsening. I feel overwhelmed and uncertain about what this means for my health. Pain medications have provided minimal relief.",
        "Cleaned Text": "31-year-old Asian female multiple myeloma severe pain back legs started a week ago worsening feel overwhelmed uncertain health pain medications minimal relief",
        "Pain Intensity": "Severe",
        "Pain Type": "pain",
        "Body Part": "back and legs",
        "Duration": "a week ago",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 41-year-old White male with liver cancer, and I have been experiencing a dull, throbbing pain in my right side for several weeks now. While it's frustrating, I keep a positive attitude and use relaxation techniques to manage it.",
        "Cleaned Text": "41-year-old White male liver cancer dull throbbing pain right side several weeks frustrating keep positive attitude use relaxation techniques manage",
        "Pain Intensity": "Moderate",
        "Pain Type": "throbbing",
        "Body Part": "right side",
        "Duration": "several weeks",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 36-year-old Black female diagnosed with pancreatic cancer who experiences sharp pain in my abdomen that worsens after eating. This has been happening for about two weeks, and it's concerning me deeply. I’m trying to eat smaller meals to see if that helps.",
        "Cleaned Text": "36-year-old Black female pancreatic cancer sharp pain abdomen worsen after eating about two weeks concerning deeply trying eat smaller meals help",
        "Pain Intensity": "Severe",
        "Pain Type": "sharp",
        "Body Part": "abdomen",
        "Duration": "about two weeks",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 26-year-old Hispanic male with skin cancer, and I sometimes feel a burning sensation in the area of my treatment. It's uncomfortable, but I’m learning to cope with it. I believe it will get better as my treatment continues.",
        "Cleaned Text": "26-year-old Hispanic male skin cancer sometimes feel burning sensation area treatment uncomfortable learning cope believe get better treatment continues",
        "Pain Intensity": "Moderate",
        "Pain Type": "burning",
        "Body Part": "treatment area",
        "Duration": "sometimes",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 59-year-old Caucasian female with esophageal cancer who feels severe pain in my chest that radiates to my back. This pain started abruptly last night and has not subsided. I am frightened and unsure about what it means for my health.",
        "Cleaned Text": "59-year-old Caucasian female esophageal cancer severe pain chest radiate back started abruptly last night not subside frightened unsure health",
        "Pain Intensity": "Severe",
        "Pain Type": "pain",
        "Body Part": "chest",
        "Duration": "last night",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 34-year-old Black female diagnosed with thyroid cancer who experiences intermittent pain in my neck. While it’s not constant, it can be sharp and quite annoying at times. I’m trying to focus on the positives in my journey.",
        "Cleaned Text": "34-year-old Black female thyroid cancer intermittent pain neck not constant sharp annoying times trying focus positives journey",
        "Pain Intensity": "Moderate",
        "Pain Type": "sharp",
        "Body Part": "neck",
        "Duration": "intermittent",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 48-year-old Asian male with kidney cancer, experiencing a steady, nagging pain in my side for the last week. While it’s bothersome, I am grateful for my family’s support during this time.",
        "Cleaned Text": "48-year-old Asian male kidney cancer steady nagging pain side last week bothersome grateful family support time",
        "Pain Intensity": "Moderate",
        "Pain Type": "nagging",
        "Body Part": "side",
        "Duration": "last week",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 39-year-old Hispanic female with stomach cancer experiencing intense pain that feels like pressure in my abdomen. This has been ongoing for three days, and it worries me. I’m doing my best to manage it with meditation.",
        "Cleaned Text": "39-year-old Hispanic female stomach cancer intense pain pressure abdomen ongoing three days worries doing best manage meditation",
        "Pain Intensity": "Severe",
        "Pain Type": "pressure",
        "Body Part": "abdomen",
        "Duration": "three days",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 53-year-old Caucasian male diagnosed with testicular cancer. I sometimes feel mild discomfort in my lower abdomen. While it's not severe, it can be distracting. I try to remind myself that I am in the right treatment program.",
        "Cleaned Text": "53-year-old Caucasian male testicular cancer sometimes feel mild discomfort lower abdomen not severe distracting try remind in right treatment program",
        "Pain Intensity": "Mild",
        "Pain Type": "discomfort",
        "Body Part": "lower abdomen",
        "Duration": "sometimes",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 61-year-old Asian female with uterine cancer, and I feel a constant ache in my lower back. This has been troubling me for the last month. It’s frustrating, but I remain hopeful about my recovery.",
        "Cleaned Text": "61-year-old Asian female uterine cancer constant ache lower back troubling last month frustrating remain hopeful recovery",
        "Pain Intensity": "Moderate",
        "Pain Type": "ache",
        "Body Part": "lower back",
        "Duration": "last month",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 40-year-old Black male with colon cancer, and I've been having sharp pains in my lower abdomen. This started a few days ago and is concerning. I am eager to discuss this with my doctor during my next appointment.",
        "Cleaned Text": "40-year-old Black male colon cancer sharp pains lower abdomen started few days concerning eager discuss doctor next appointment",
        "Pain Intensity": "Severe",
        "Pain Type": "sharp",
        "Body Part": "lower abdomen",
        "Duration": "a few days",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 28-year-old Hispanic female with brain cancer who has been experiencing mild headaches intermittently. Although they can be bothersome, I stay active and continue my work as it keeps my spirits up.",
        "Cleaned Text": "28-year-old Hispanic female brain cancer mild headaches intermittently bothersome stay active continue work keeps spirits up",
        "Pain Intensity": "Mild",
        "Pain Type": "headaches",
        "Body Part": "head",
        "Duration": "intermittently",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 46-year-old Caucasian male with lung cancer, and I experience a dull pain in my chest that seems to be getting worse. It’s concerning, but I’m trying to remain strong and focus on the positive aspects of my life.",
        "Cleaned Text": "46-year-old Caucasian male lung cancer dull pain chest getting worse concerning trying remain strong focus positive aspects life",
        "Pain Intensity": "Moderate",
        "Pain Type": "dull",
        "Body Part": "chest",
        "Duration": "getting worse",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 35-year-old Black female with ovarian cancer, and I feel a constant throbbing pain in my abdomen. This has been ongoing for about a week now and is quite alarming. I plan to contact my doctor for advice.",
        "Cleaned Text": "35-year-old Black female ovarian cancer constant throbbing pain abdomen ongoing about a week quite alarming plan contact doctor advice",
        "Pain Intensity": "Severe",
        "Pain Type": "throbbing",
        "Body Part": "abdomen",
        "Duration": "about a week",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 55-year-old Asian male with esophageal cancer who feels a slight burning sensation in my throat. It's not painful, but it's uncomfortable enough to notice. I’m hopeful this will improve as I progress through treatment.",
        "Cleaned Text": "55-year-old Asian male esophageal cancer slight burning sensation throat not painful uncomfortable enough notice hopeful improve progress treatment",
        "Pain Intensity": "Mild",
        "Pain Type": "burning",
        "Body Part": "throat",
        "Duration": "notice",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 62-year-old Hispanic female with breast cancer experiencing severe pain in my left arm that started suddenly. I am deeply concerned about it, and despite trying pain medications, it has not improved.",
        "Cleaned Text": "62-year-old Hispanic female breast cancer severe pain left arm started suddenly deeply concerned despite trying pain medications not improved",
        "Pain Intensity": "Severe",
        "Pain Type": "pain",
        "Body Part": "left arm",
        "Duration": "started suddenly",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 30-year-old Black male with leukemia, and I have been experiencing intermittent mild headaches. They can be annoying, but I try to manage them with rest and hydration. Overall, I feel hopeful about my treatment.",
        "Cleaned Text": "30-year-old Black male leukemia intermittent mild headaches annoying manage rest hydration feel hopeful treatment",
        "Pain Intensity": "Mild",
        "Pain Type": "headaches",
        "Body Part": "head",
        "Duration": "intermittent",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 37-year-old Caucasian female with colorectal cancer who feels a constant pressure in my lower abdomen. This has been going on for several days, and I am worried about what it might mean. I’m trying to stay calm.",
        "Cleaned Text": "37-year-old Caucasian female colorectal cancer constant pressure lower abdomen several days worried trying stay calm",
        "Pain Intensity": "Moderate",
        "Pain Type": "pressure",
        "Body Part": "lower abdomen",
        "Duration": "several days",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 49-year-old Hispanic male with prostate cancer, and I experience a nagging pain in my right hip that comes and goes. It’s frustrating at times, but I try to focus on my family and the support they provide.",
        "Cleaned Text": "49-year-old Hispanic male prostate cancer nagging pain right hip comes goes frustrating times focus family support provide",
        "Pain Intensity": "Moderate",
        "Pain Type": "nagging",
        "Body Part": "right hip",
        "Duration": "comes and goes",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 52-year-old Asian female with lung cancer who has been experiencing sharp, stabbing pains in my chest. This started a few days ago, and I am very worried about it. I have an appointment with my doctor soon.",
        "Cleaned Text": "52-year-old Asian female lung cancer sharp stabbing pains chest started few days very worried appointment doctor soon",
        "Pain Intensity": "Severe",
        "Pain Type": "stabbing",
        "Body Part": "chest",
        "Duration": "a few days",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 43-year-old Black male with kidney cancer, and I sometimes feel a dull ache in my lower back. It’s not too bad, and I try to manage it with exercises. Overall, I maintain a positive outlook.",
        "Cleaned Text": "43-year-old Black male kidney cancer sometimes feel dull ache lower back not too bad manage exercises maintain positive outlook",
        "Pain Intensity": "Mild",
        "Pain Type": "ache",
        "Body Part": "lower back",
        "Duration": "sometimes",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 58-year-old Caucasian female with pancreatic cancer experiencing severe discomfort in my abdomen. This started a week ago, and it has made me anxious. I’m hoping for some relief soon.",
        "Cleaned Text": "58-year-old Caucasian female pancreatic cancer severe discomfort abdomen started week ago made anxious hoping relief soon",
        "Pain Intensity": "Severe",
        "Pain Type": "discomfort",
        "Body Part": "abdomen",
        "Duration": "a week ago",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 29-year-old Asian male with testicular cancer who occasionally feels sharp pain in my groin. While it can be alarming, I try to remain optimistic and focus on my health.",
        "Cleaned Text": "29-year-old Asian male testicular cancer occasionally feels sharp pain groin alarming try remain optimistic focus health",
        "Pain Intensity": "Moderate",
        "Pain Type": "sharp",
        "Body Part": "groin",
        "Duration": "occasionally",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 63-year-old Hispanic female with liver cancer experiencing severe pain in my right flank. This has been happening for about two weeks now. I feel scared and uncertain about my prognosis.",
        "Cleaned Text": "63-year-old Hispanic female liver cancer severe pain right flank happening about two weeks scared uncertain prognosis",
        "Pain Intensity": "Severe",
        "Pain Type": "pain",
        "Body Part": "right flank",
        "Duration": "about two weeks",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 41-year-old Caucasian male with multiple myeloma, and I experience mild discomfort in my joints. It’s not severe, and I try to keep active and stay positive.",
        "Cleaned Text": "41-year-old Caucasian male multiple myeloma mild discomfort joints not severe try keep active stay positive",
        "Pain Intensity": "Mild",
        "Pain Type": "discomfort",
        "Body Part": "joints",
        "Duration": "mild",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 50-year-old Black female with stomach cancer experiencing sharp pain in my lower abdomen. This started suddenly and is concerning me greatly. I am going to contact my doctor to discuss it.",
        "Cleaned Text": "50-year-old Black female stomach cancer sharp pain lower abdomen started suddenly concerning greatly going contact doctor discuss",
        "Pain Intensity": "Severe",
        "Pain Type": "sharp",
        "Body Part": "lower abdomen",
        "Duration": "suddenly",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 27-year-old Hispanic male with brain cancer who occasionally feels a dull ache in my head. It’s not too bad, and I manage it with simple over-the-counter medications. I try to stay positive.",
        "Cleaned Text": "27-year-old Hispanic male brain cancer occasionally feels dull ache head not too bad manage simple over-the-counter medications try stay positive",
        "Pain Intensity": "Mild",
        "Pain Type": "dull ache",
        "Body Part": "head",
        "Duration": "occasionally",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 59-year-old Caucasian female with breast cancer experiencing severe pain in my lower back. This pain started after my last treatment and has been relentless. I feel worried and uncertain about my recovery.",
        "Cleaned Text": "59-year-old Caucasian female breast cancer severe pain lower back started last treatment relentless worried uncertain recovery",
        "Pain Intensity": "Severe",
        "Pain Type": "pain",
        "Body Part": "lower back",
        "Duration": "after last treatment",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 46-year-old Asian male with colorectal cancer who experiences intermittent sharp pain in my abdomen. While it’s not constant, it can be alarming. I focus on the support from my family, which helps.",
        "Cleaned Text": "46-year-old Asian male colorectal cancer intermittent sharp pain abdomen not constant alarming focus support family helps",
        "Pain Intensity": "Moderate",
        "Pain Type": "sharp",
        "Body Part": "abdomen",
        "Duration": "intermittent",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 53-year-old Black female with ovarian cancer, and I feel a constant pain in my lower back that has persisted for a week. It's very troubling, and I’m anxious about what this could mean.",
        "Cleaned Text": "53-year-old Black female ovarian cancer constant pain lower back persisted week troubling anxious could mean",
        "Pain Intensity": "Severe",
        "Pain Type": "pain",
        "Body Part": "lower back",
        "Duration": "for a week",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 34-year-old Hispanic male with lung cancer who sometimes feels a mild ache in my chest. It’s manageable, and I try to keep my spirits high.",
        "Cleaned Text": "34-year-old Hispanic male lung cancer sometimes feels mild ache chest manageable try keep spirits high",
        "Pain Intensity": "Mild",
        "Pain Type": "ache",
        "Body Part": "chest",
        "Duration": "sometimes",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 48-year-old Asian female with kidney cancer, and I experience sharp pain in my right side that started suddenly. This is alarming, and I plan to see my doctor soon.",
        "Cleaned Text": "48-year-old Asian female kidney cancer sharp pain right side started suddenly alarming plan see doctor soon",
        "Pain Intensity": "Severe",
        "Pain Type": "sharp",
        "Body Part": "right side",
        "Duration": "started suddenly",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 42-year-old Caucasian male with bladder cancer who sometimes feels a nagging pain in my abdomen. While it’s bothersome, I stay positive and focused on my treatment.",
        "Cleaned Text": "42-year-old Caucasian male bladder cancer sometimes feels nagging pain abdomen bothersome stay positive focused treatment",
        "Pain Intensity": "Moderate",
        "Pain Type": "nagging",
        "Body Part": "abdomen",
        "Duration": "sometimes",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 61-year-old Black female with pancreatic cancer experiencing severe pain in my stomach that started last week. It’s very distressing, and I feel anxious about my condition.",
        "Cleaned Text": "61-year-old Black female pancreatic cancer severe pain stomach started last week very distressing anxious condition",
        "Pain Intensity": "Severe",
        "Pain Type": "pain",
        "Body Part": "stomach",
        "Duration": "last week",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 55-year-old Asian male diagnosed with multiple myeloma experiencing mild pain in my joints. It’s manageable, and I maintain a positive outlook through my treatment journey.",
        "Cleaned Text": "55-year-old Asian male multiple myeloma mild pain joints manageable maintain positive outlook treatment journey",
        "Pain Intensity": "Mild",
        "Pain Type": "pain",
        "Body Part": "joints",
        "Duration": "manageable",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 39-year-old Hispanic female with breast cancer experiencing sharp pain in my right side. This pain started suddenly a few days ago, and it worries me greatly.",
        "Cleaned Text": "39-year-old Hispanic female breast cancer sharp pain right side started suddenly few days ago worries greatly",
        "Pain Intensity": "Severe",
        "Pain Type": "sharp",
        "Body Part": "right side",
        "Duration": "few days ago",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 29-year-old Caucasian male with testicular cancer who experiences dull, nagging pain in my lower abdomen. It’s not severe, but it can be distracting at times. I try to focus on my treatment.",
        "Cleaned Text": "29-year-old Caucasian male testicular cancer dull nagging pain lower abdomen not severe distracting times try focus treatment",
        "Pain Intensity": "Mild",
        "Pain Type": "nagging",
        "Body Part": "lower abdomen",
        "Duration": "sometimes",
        "Sentiment": "Positive"
    },
    {
        "Original Text": "I am a 64-year-old Black female with lung cancer experiencing severe pain in my chest that feels like a weight pressing down. This started abruptly last night and has not improved. I am feeling anxious about this.",
        "Cleaned Text": "64-year-old Black female lung cancer severe pain chest feels weight pressing down started abruptly last night not improved feeling anxious",
        "Pain Intensity": "Severe",
        "Pain Type": "pressure",
        "Body Part": "chest",
        "Duration": "last night",
        "Sentiment": "Negative"
    },
    {
        "Original Text": "I am a 45-year-old Asian male with prostate cancer who sometimes feels mild discomfort in my lower back. It's manageable, and I am trying to stay active and engaged.",
        "Cleaned Text": "45-year-old Asian male prostate cancer sometimes feels mild discomfort lower back manageable trying stay active engaged",
        "Pain Intensity": "Mild",
        "Pain Type": "discomfort",
        "Body Part": "lower back",
        "Duration": "sometimes",
        "Sentiment": "Positive"
    },
    {
        "Input Text": "I am a 39-year-old woman with cervical cancer, experiencing a dull ache in my neck that has persisted for two weeks. It’s a constant reminder of my illness, making me feel sad and overwhelmed. I’ve been trying to manage it with relaxation techniques but have found limited relief.",
        "Cleaned Text": "dull ache neck persist two weeks constant reminder illness feel sad overwhelmed trying manage relaxation techniques limited relief",
        "Pain Intensity": "Moderate",
        "Pain Type": "Dull ache",
        "Body Part": "Neck",
        "Duration": "Two weeks",
        "Sentiment": "Overwhelmed"
    },
    {
        "Input Text": "I am a 50-year-old male diagnosed with prostate cancer. I've been experiencing a throbbing pain in my pelvic area for the last month. It feels frustrating, especially when I try to engage in physical activity.",
        "Cleaned Text": "throbbing pain pelvic area last month feel frustrating try engage physical activity",
        "Pain Intensity": "Moderate",
        "Pain Type": "Throbbing",
        "Body Part": "Pelvic area",
        "Duration": "Last month",
        "Sentiment": "Frustrated"
    },
    {
        "Input Text": "As a 65-year-old woman with ovarian cancer, I’ve had a constant sharp pain in my abdomen for the past week. It’s worrying, and I often feel anxious about the implications.",
        "Cleaned Text": "constant sharp pain abdomen past week worrying often feel anxious implications",
        "Pain Intensity": "Severe",
        "Pain Type": "Sharp",
        "Body Part": "Abdomen",
        "Duration": "Past week",
        "Sentiment": "Anxious"
    },
    {
        "Input Text": "I am a 30-year-old female with a history of cervical cancer, experiencing a burning sensation in my lower abdomen for the past three days. This pain is alarming and makes me feel helpless.",
        "Cleaned Text": "burning sensation lower abdomen past three days pain alarming feel helpless",
        "Pain Intensity": "Moderate",
        "Pain Type": "Burning",
        "Body Part": "Lower abdomen",
        "Duration": "Past three days",
        "Sentiment": "Helpless"
    },
    {
        "Input Text": "I am a 42-year-old male suffering from multiple myeloma. I have been dealing with mild discomfort in my ribs for two weeks, and it's making me feel discouraged.",
        "Cleaned Text": "mild discomfort ribs two weeks making feel discouraged",
        "Pain Intensity": "Mild",
        "Pain Type": "Discomfort",
        "Body Part": "Ribs",
        "Duration": "Two weeks",
        "Sentiment": "Discouraged"
    },
    {
        "Input Text": "As a 67-year-old female with lung cancer, I’ve been experiencing severe shortness of breath and chest pain for the last few days. It's distressing and affecting my ability to rest.",
        "Cleaned Text": "severe shortness breath chest pain last few days distressing affecting ability rest",
        "Pain Intensity": "Severe",
        "Pain Type": "Chest pain",
        "Body Part": "Chest",
        "Duration": "Last few days",
        "Sentiment": "Distressed"
    },
    {
        "Input Text": "I’m a 38-year-old woman undergoing treatment for breast cancer. I have a nagging pain in my right side that has lasted for a week. It’s frustrating as I want to feel better.",
        "Cleaned Text": "nagging pain right side lasted week frustrating want feel better",
        "Pain Intensity": "Moderate",
        "Pain Type": "Nagging",
        "Body Part": "Right side",
        "Duration": "Lasted week",
        "Sentiment": "Frustrated"
    },
    {
        "Input Text": "I am a 73-year-old man diagnosed with colorectal cancer. I've had sharp, intermittent pain in my abdomen for the past month. This unpredictability makes me feel uneasy.",
        "Cleaned Text": "sharp intermittent pain abdomen past month unpredictability feel uneasy",
        "Pain Intensity": "Severe",
        "Pain Type": "Sharp",
        "Body Part": "Abdomen",
        "Duration": "Past month",
        "Sentiment": "Uneasy"
    },
    {
        "Input Text": "As a 62-year-old female with a history of leukemia, I've been experiencing a mild headache that has persisted for two weeks. It’s annoying and impacts my focus.",
        "Cleaned Text": "mild headache persisted two weeks annoying impacts focus",
        "Pain Intensity": "Mild",
        "Pain Type": "Headache",
        "Body Part": "Head",
        "Duration": "Two weeks",
        "Sentiment": "Annoyed"
    },
    {
        "Input Text": "I am a 48-year-old male with liver cancer. I have been feeling severe pain in my upper right abdomen for the last five days. It's overwhelming, and I’m worried about my future.",
        "Cleaned Text": "severe pain upper right abdomen last five days overwhelming worried future",
        "Pain Intensity": "Severe",
        "Pain Type": "Pain",
        "Body Part": "Upper right abdomen",
        "Duration": "Last five days",
        "Sentiment": "Worried"
    },
    {
        "Input Text": "I’m a 34-year-old female with thyroid cancer experiencing a constant ache in my throat for the last two weeks. It’s frustrating and makes swallowing difficult.",
        "Cleaned Text": "constant ache throat last two weeks frustrating makes swallowing difficult",
        "Pain Intensity": "Moderate",
        "Pain Type": "Ache",
        "Body Part": "Throat",
        "Duration": "Last two weeks",
        "Sentiment": "Frustrated"
    },
    {
        "Input Text": "As a 58-year-old male diagnosed with melanoma, I experience sharp pain in my right leg for the past week. This pain affects my mobility and makes me feel upset.",
        "Cleaned Text": "sharp pain right leg past week affects mobility makes feel upset",
        "Pain Intensity": "Severe",
        "Pain Type": "Sharp",
        "Body Part": "Right leg",
        "Duration": "Past week",
        "Sentiment": "Upset"
    },
    {
        "Input Text": "I am a 45-year-old female with ovarian cancer. I have a mild pain in my back that has been present for about a week. It’s concerning, but I am trying to stay optimistic.",
        "Cleaned Text": "mild pain back present about week concerning trying stay optimistic",
        "Pain Intensity": "Mild",
        "Pain Type": "Pain",
        "Body Part": "Back",
        "Duration": "About a week",
        "Sentiment": "Optimistic"
    },
    {
        "Input Text": "I am a 70-year-old man with esophageal cancer. I have severe pain while swallowing that has been ongoing for several days. It’s distressing and makes me feel fearful.",
        "Cleaned Text": "severe pain swallowing ongoing several days distressing makes feel fearful",
        "Pain Intensity": "Severe",
        "Pain Type": "Pain",
        "Body Part": "Esophagus",
        "Duration": "Ongoing for several days",
        "Sentiment": "Fearful"
    },
    {
        "Input Text": "As a 39-year-old woman with cervical cancer, I’ve experienced a sharp pain in my pelvic area for two weeks. It’s bothersome, but I’m hopeful about my treatment.",
        "Cleaned Text": "sharp pain pelvic area two weeks bothersome hopeful treatment",
        "Pain Intensity": "Moderate",
        "Pain Type": "Sharp",
        "Body Part": "Pelvic area",
        "Duration": "Two weeks",
        "Sentiment": "Hopeful"
    },
    {
        "Input Text": "I’m a 65-year-old female with breast cancer. I’ve had mild discomfort in my breast for a few days. It’s worrying, but I’m trying to remain calm.",
        "Cleaned Text": "mild discomfort breast few days worrying trying remain calm",
        "Pain Intensity": "Mild",
        "Pain Type": "Discomfort",
        "Body Part": "Breast",
        "Duration": "Few days",
        "Sentiment": "Calm"
    },
    {
        "Input Text": "As a 56-year-old male with lung cancer, I have severe pain in my chest and difficulty breathing for about a week. This situation is overwhelming and makes me feel hopeless.",
        "Cleaned Text": "severe pain chest difficulty breathing about week overwhelming makes feel hopeless",
        "Pain Intensity": "Severe",
        "Pain Type": "Pain",
        "Body Part": "Chest",
        "Duration": "About a week",
        "Sentiment": "Hopeless"
    },
    {
        "Input Text": "Im a 72-year-old woman diagnosed with pancreatic cancer. Ive had a constant ache in my stomach for several weeks. It’s frustrating, but I’m trying to manage my symptoms.",
        "Cleaned Text": "constant ache stomach several weeks frustrating trying manage symptoms",
        "Pain Intensity": "Moderate",
        "Pain Type": "Ache",
        "Body Part": "Stomach",
        "Duration": "Several weeks",
        "Sentiment": "Frustrated"
    },
    {
        "Input Text": "I am a 61-year-old male with colorectal cancer. I have been suffering from sharp pain in my abdomen for a few days. It’s alarming, and I often feel anxious.",
        "Cleaned Text": "sharp pain abdomen few days alarming often feel anxious",
        "Pain Intensity": "Severe",
        "Pain Type": "Sharp",
        "Body Part": "Abdomen",
        "Duration": "Few days",
        "Sentiment": "Anxious"
    },
    {
        "Input Text": "As a 44-year-old woman with a history of kidney cancer, I am experiencing mild discomfort in my side for about a week. It’s manageable, but I remain vigilant.",
        "Cleaned Text": "mild discomfort side about week manageable remain vigilant",
        "Pain Intensity": "Mild",
        "Pain Type": "Discomfort",
        "Body Part": "Side",
        "Duration": "About a week",
        "Sentiment": "Vigilant"
    },
]

print(len(data))

for i in data:
    try:
       print(i["Original Text"])
       i["Input Text"] = i["Original Text"]
       del i["Original Text"] 

    except:
        continue

print(len(data))

# Create DataFrame
df = pd.DataFrame(data)

# len of dataframe
len(df)

# Expand the dataset to include 100 unique entries
# For the sake of brevity, I'm adding a few more entries. You would need to expand this to 100.
additional_entries = [
    {
        "Input Text": "I'm a 70-year-old female diagnosed with endometrial cancer, experiencing moderate pain in my lower back for the past month. It's a nagging pain that makes daily tasks challenging, and I often feel overwhelmed. I’m trying to stay positive and focus on my treatment.",
        "Cleaned Text": "moderate pain lower back past month nagging pain make daily tasks challenging often feel overwhelmed trying stay positive focus treatment",
        "Pain Intensity": "Moderate",
        "Pain Type": "Nagging",
        "Body Part": "Lower back",
        "Duration": "Past month",
        "Sentiment": "Overwhelmed"
    },
    {
        "Input Text": "I am a 55-year-old woman diagnosed with pancreatic cancer. I have been suffering from excruciating back pain that radiates down my spine for about three weeks. It’s overwhelming and has left me feeling helpless. I’ve tried physical therapy, but it’s just not enough.",
        "Cleaned Text": "excruciating back pain radiate down spine about three weeks overwhelming feel helpless tried physical therapy not enough",
        "Pain Intensity": "Severe",
        "Pain Type": "Excruciating",
        "Body Part": "Back",
        "Duration": "About three weeks",
        "Sentiment": "Helpless"
    },
    # Continue adding more entries...
]

# Append additional entries to the DataFrame
df = pd.concat([df, pd.DataFrame(additional_entries)], ignore_index=True)

# Ensure the DataFrame contains 100 entries (repeat or vary existing entries if needed)
while len(df) < 100:
    df = pd.concat([df, df.sample(n=1)], ignore_index=True)

# Save the dataset to a CSV file
df.to_csv('cancer_pain_data.csv', index=False)

print("Dataset created and saved as 'cancer_pain_data.csv'")

# ------------------------------------------------------------

# Expanded sample data entries
data_entries = [
    {"Input Text": "I have a severe stabbing pain in my lower back that has persisted for the last two weeks.", "Cleaned Text": "severe stabbing pain lower back persist last two week", "Pain Intensity": "Severe", "Pain Type": "stabbing", "Body Part": "lower back", "Duration": "for the last two weeks", "Sentiment": "Negative"},
    {"Input Text": "There’s a constant dull ache in my abdomen that’s been bothering me for about three days now.", "Cleaned Text": "constant dull ache abdomen bother about three day now", "Pain Intensity": "Moderate", "Pain Type": "dull", "Body Part": "abdomen", "Duration": "about three days", "Sentiment": "Negative"},
    {"Input Text": "I've been experiencing intermittent sharp pain in my chest that worsens when I breathe deeply.", "Cleaned Text": "experience intermittent sharp pain chest worsen breathe deeply", "Pain Intensity": "Severe", "Pain Type": "sharp", "Body Part": "chest", "Duration": "intermittent", "Sentiment": "Negative"},
    {"Input Text": "I feel a mild throbbing pain in my right shoulder that comes and goes throughout the day.", "Cleaned Text": "feel mild throbbing pain right shoulder come go throughout day", "Pain Intensity": "Mild", "Pain Type": "throbbing", "Body Part": "right shoulder", "Duration": "comes and goes", "Sentiment": "Negative"},
    {"Input Text": "There is an excruciating pain in my left leg that started after my last chemotherapy session.", "Cleaned Text": "excruciating pain left leg start last chemotherapy session", "Pain Intensity": "Severe", "Pain Type": "excruciating", "Body Part": "left leg", "Duration": "after last chemotherapy session", "Sentiment": "Negative"},
    {"Input Text": "I have a burning sensation in my stomach that has lasted for several hours.", "Cleaned Text": "burning sensation stomach last several hour", "Pain Intensity": "Moderate", "Pain Type": "burning", "Body Part": "stomach", "Duration": "for several hours", "Sentiment": "Negative"},
    {"Input Text": "There’s a persistent aching pain in my lower back that I’ve had for nearly a week.", "Cleaned Text": "persistent aching pain lower back have nearly week", "Pain Intensity": "Moderate", "Pain Type": "aching", "Body Part": "lower back", "Duration": "for nearly a week", "Sentiment": "Negative"},
    {"Input Text": "My right arm feels weak and there's a sharp pain when I lift anything heavy.", "Cleaned Text": "right arm feel weak sharp pain lift anything heavy", "Pain Intensity": "Moderate", "Pain Type": "sharp", "Body Part": "right arm", "Duration": "when lifting", "Sentiment": "Negative"},
    {"Input Text": "I occasionally experience a shooting pain in my neck, especially when turning my head.", "Cleaned Text": "occasionally experience shooting pain neck especially turning head", "Pain Intensity": "Moderate", "Pain Type": "shooting", "Body Part": "neck", "Duration": "occasionally", "Sentiment": "Negative"},
    {"Input Text": "There's a consistent throbbing pain in my head that has been bothering me for over a week.", "Cleaned Text": "consistent throbbing pain head bother over week", "Pain Intensity": "Moderate", "Pain Type": "throbbing", "Body Part": "head", "Duration": "for over a week", "Sentiment": "Negative"},
    {"Input Text": "I feel a sharp pain in my abdomen that comes after eating.", "Cleaned Text": "feel sharp pain abdomen come after eat", "Pain Intensity": "Moderate", "Pain Type": "sharp", "Body Part": "abdomen", "Duration": "after eating", "Sentiment": "Negative"},
    {"Input Text": "I've had a dull pain in my back for the past few days, and it’s making it hard to sleep.", "Cleaned Text": "dull pain back past few day make hard sleep", "Pain Intensity": "Moderate", "Pain Type": "dull", "Body Part": "back", "Duration": "for the past few days", "Sentiment": "Negative"},
    {"Input Text": "My pain in the lower back has been very intense after my treatment last week.", "Cleaned Text": "pain lower back intense treatment last week", "Pain Intensity": "Severe", "Pain Type": "intense", "Body Part": "lower back", "Duration": "after treatment last week", "Sentiment": "Negative"},
    {"Input Text": "There’s a nagging pain in my side that has persisted for about a month.", "Cleaned Text": "nagging pain side persist about month", "Pain Intensity": "Moderate", "Pain Type": "nagging", "Body Part": "side", "Duration": "for about a month", "Sentiment": "Negative"},
    {"Input Text": "I have a sharp, radiating pain in my left arm that worries me.", "Cleaned Text": "sharp radiating pain left arm worry", "Pain Intensity": "Severe", "Pain Type": "radiating", "Body Part": "left arm", "Duration": "N/A", "Sentiment": "Negative"},
    {"Input Text": "I sometimes feel a dull ache in my joints that has been persistent for weeks.", "Cleaned Text": "sometimes feel dull ache joint persistent weeks", "Pain Intensity": "Mild", "Pain Type": "dull", "Body Part": "joints", "Duration": "for weeks", "Sentiment": "Negative"},
    {"Input Text": "After my last session of radiation, I felt a burning pain in my throat.", "Cleaned Text": "last session radiation feel burning pain throat", "Pain Intensity": "Moderate", "Pain Type": "burning", "Body Part": "throat", "Duration": "after last session", "Sentiment": "Negative"},
    {"Input Text": "I experience sharp pain in my right knee when I walk.", "Cleaned Text": "experience sharp pain right knee walk", "Pain Intensity": "Moderate", "Pain Type": "sharp", "Body Part": "right knee", "Duration": "when walking", "Sentiment": "Negative"},
    {"Input Text": "I feel fine most of the time, but occasionally I have a slight pain in my lower back.", "Cleaned Text": "feel fine most time occasionally slight pain lower back", "Pain Intensity": "Mild", "Pain Type": "slight", "Body Part": "lower back", "Duration": "occasionally", "Sentiment": "Positive"},
    {"Input Text": "There's a throbbing pain in my head that started after I began my medication.", "Cleaned Text": "throbbing pain head start begin medication", "Pain Intensity": "Moderate", "Pain Type": "throbbing", "Body Part": "head", "Duration": "after starting medication", "Sentiment": "Negative"},
    {"Input Text": "I have a sharp, stabbing pain in my chest that feels worse when I breathe deeply.", "Cleaned Text": "sharp stabbing pain chest feel worse breathe deeply", "Pain Intensity": "Severe", "Pain Type": "stabbing", "Body Part": "chest", "Duration": "when breathing deeply", "Sentiment": "Negative"},
    {"Input Text": "I've been having a nagging pain in my lower abdomen for several weeks now.", "Cleaned Text": "having nagging pain lower abdomen several week now", "Pain Intensity": "Moderate", "Pain Type": "nagging", "Body Part": "lower abdomen", "Duration": "for several weeks", "Sentiment": "Negative"},
    {"Input Text": "There’s a persistent pain in my right thigh that I can’t seem to shake off.", "Cleaned Text": "persistent pain right thigh cant seem shake off", "Pain Intensity": "Moderate", "Pain Type": "persistent", "Body Part": "right thigh", "Duration": "N/A", "Sentiment": "Negative"},
    {"Input Text": "I feel occasional sharp pains in my back, especially after sitting for a long time.", "Cleaned Text": "feel occasional sharp pain back especially sitting long time", "Pain Intensity": "Moderate", "Pain Type": "sharp", "Body Part": "back", "Duration": "after sitting", "Sentiment": "Negative"},
    {"Input Text": "After chemotherapy, I experienced a severe ache in my lower back that hasn’t gone away.", "Cleaned Text": "after chemotherapy experience severe ache lower back not go away", "Pain Intensity": "Severe", "Pain Type": "ache", "Body Part": "lower back", "Duration": "after chemotherapy", "Sentiment": "Negative"},
    {"Input Text": "I have a constant, dull pain in my left side that’s been there for a few days.", "Cleaned Text": "constant dull pain left side been there few day", "Pain Intensity": "Moderate", "Pain Type": "dull", "Body Part": "left side", "Duration": "for a few days", "Sentiment": "Negative"},
    {"Input Text": "There’s a sharp pain in my side whenever I move quickly.", "Cleaned Text": "sharp pain side whenever move quickly", "Pain Intensity": "Moderate", "Pain Type": "sharp", "Body Part": "side", "Duration": "whenever moving quickly", "Sentiment": "Negative"},
    {"Input Text": "I feel a throbbing sensation in my upper back that intensifies at night.", "Cleaned Text": "throbbing sensation upper back intensify night", "Pain Intensity": "Moderate", "Pain Type": "throbbing", "Body Part": "upper back", "Duration": "at night", "Sentiment": "Negative"},
    {"Input Text": "My legs feel heavy, and I have a constant pain that feels like cramping.", "Cleaned Text": "legs feel heavy constant pain feel cramping", "Pain Intensity": "Moderate", "Pain Type": "cramping", "Body Part": "legs", "Duration": "constant", "Sentiment": "Negative"},
    {"Input Text": "I experience sharp pains in my throat that make swallowing difficult.", "Cleaned Text": "experience sharp pain throat make swallowing difficult", "Pain Intensity": "Severe", "Pain Type": "sharp", "Body Part": "throat", "Duration": "when swallowing", "Sentiment": "Negative"},
    {"Input Text": "After my last treatment, I have a dull, persistent ache in my side.", "Cleaned Text": "after last treatment have dull persistent ache side", "Pain Intensity": "Moderate", "Pain Type": "dull", "Body Part": "side", "Duration": "after treatment", "Sentiment": "Negative"},
    {"Input Text": "I feel a sharp, burning sensation in my chest that worries me.", "Cleaned Text": "feel sharp burning sensation chest worry", "Pain Intensity": "Severe", "Pain Type": "burning", "Body Part": "chest", "Duration": "N/A", "Sentiment": "Negative"},
    {"Input Text": "There’s an occasional twinge of pain in my lower back that lasts only for a moment.", "Cleaned Text": "occasional twinge pain lower back last moment", "Pain Intensity": "Mild", "Pain Type": "twinge", "Body Part": "lower back", "Duration": "only for a moment", "Sentiment": "Positive"},
    {"Input Text": "I experience a sharp, stabbing pain in my abdomen, especially after meals.", "Cleaned Text": "experience sharp stabbing pain abdomen especially after meal", "Pain Intensity": "Severe", "Pain Type": "stabbing", "Body Part": "abdomen", "Duration": "after meals", "Sentiment": "Negative"},
    {"Input Text": "After treatment, I have a dull, aching sensation in my lower back that doesn’t go away.", "Cleaned Text": "after treatment have dull aching sensation lower back not go away", "Pain Intensity": "Moderate", "Pain Type": "aching", "Body Part": "lower back", "Duration": "after treatment", "Sentiment": "Negative"},
    {"Input Text": "My fingers often feel numb and painful, especially when I try to grip something.", "Cleaned Text": "fingers often feel numb painful especially try grip something", "Pain Intensity": "Moderate", "Pain Type": "numb", "Body Part": "fingers", "Duration": "when gripping", "Sentiment": "Negative"},
    {"Input Text": "I have a shooting pain in my lower abdomen that feels worse when I bend over.", "Cleaned Text": "shooting pain lower abdomen feel worse bend over", "Pain Intensity": "Severe", "Pain Type": "shooting", "Body Part": "lower abdomen", "Duration": "when bending over", "Sentiment": "Negative"},
    {"Input Text": "There's a nagging ache in my knee that has persisted for months now.", "Cleaned Text": "nagging ache knee persist month now", "Pain Intensity": "Moderate", "Pain Type": "nagging", "Body Part": "knee", "Duration": "for months", "Sentiment": "Negative"},
    {"Input Text": "I often feel a burning pain in my throat after eating.", "Cleaned Text": "often feel burning pain throat after eat", "Pain Intensity": "Moderate", "Pain Type": "burning", "Body Part": "throat", "Duration": "after eating", "Sentiment": "Negative"},
    {"Input Text": "My left arm often feels weak and painful, especially when lifting.", "Cleaned Text": "left arm often feel weak painful especially lifting", "Pain Intensity": "Moderate", "Pain Type": "painful", "Body Part": "left arm", "Duration": "especially when lifting", "Sentiment": "Negative"},
    {"Input Text": "I feel a sharp pain in my ribs that feels like it's getting worse over time.", "Cleaned Text": "sharp pain ribs feel get worse over time", "Pain Intensity": "Moderate", "Pain Type": "sharp", "Body Part": "ribs", "Duration": "over time", "Sentiment": "Negative"},
    {"Input Text": "I have a constant throbbing pain in my head that doesn’t seem to fade.", "Cleaned Text": "constant throbbing pain head not seem fade", "Pain Intensity": "Moderate", "Pain Type": "throbbing", "Body Part": "head", "Duration": "constant", "Sentiment": "Negative"},
    {"Input Text": "There's a dull ache in my hips that intensifies when I walk long distances.", "Cleaned Text": "dull ache hips intensify walk long distance", "Pain Intensity": "Moderate", "Pain Type": "ache", "Body Part": "hips", "Duration": "when walking long distances", "Sentiment": "Negative"},
    {"Input Text": "I have sharp, intermittent pain in my lower back that sometimes radiates down my legs.", "Cleaned Text": "sharp intermittent pain lower back sometimes radiate down legs", "Pain Intensity": "Severe", "Pain Type": "sharp", "Body Part": "lower back", "Duration": "sometimes", "Sentiment": "Negative"},
    {"Input Text": "I feel a deep, throbbing pain in my chest that worries me a lot.", "Cleaned Text": "deep throbbing pain chest worry a lot", "Pain Intensity": "Severe", "Pain Type": "throbbing", "Body Part": "chest", "Duration": "N/A", "Sentiment": "Negative"},
    {"Input Text": "There’s a sharp pain in my lower back that started after lifting something heavy.", "Cleaned Text": "sharp pain lower back start after lift something heavy", "Pain Intensity": "Moderate", "Pain Type": "sharp", "Body Part": "lower back", "Duration": "after lifting", "Sentiment": "Negative"},
    {"Input Text": "I sometimes have a slight pain in my left side that’s hard to describe.", "Cleaned Text": "sometimes slight pain left side hard describe", "Pain Intensity": "Mild", "Pain Type": "slight", "Body Part": "left side", "Duration": "sometimes", "Sentiment": "Positive"},
    {"Input Text": "After treatment, I have a burning sensation in my mouth that makes it difficult to eat.", "Cleaned Text": "after treatment have burning sensation mouth make difficult eat", "Pain Intensity": "Severe", "Pain Type": "burning", "Body Part": "mouth", "Duration": "after treatment", "Sentiment": "Negative"},
    {"Input Text": "I have a consistent pain in my neck that radiates down my arm.", "Cleaned Text": "consistent pain neck radiate down arm", "Pain Intensity": "Moderate", "Pain Type": "pain", "Body Part": "neck", "Duration": "constant", "Sentiment": "Negative"},
    {"Input Text": "There's a throbbing pain in my ankle that has been bothering me for days.", "Cleaned Text": "throbbing pain ankle bother for days", "Pain Intensity": "Moderate", "Pain Type": "throbbing", "Body Part": "ankle", "Duration": "for days", "Sentiment": "Negative"},
    {"Input Text": "I experience a stabbing pain in my side that often takes my breath away.", "Cleaned Text": "experience stabbing pain side often take breath away", "Pain Intensity": "Severe", "Pain Type": "stabbing", "Body Part": "side", "Duration": "often", "Sentiment": "Negative"},
    {"Input Text": "After my last chemotherapy session, I felt a sharp pain in my legs.", "Cleaned Text": "after last chemotherapy session feel sharp pain legs", "Pain Intensity": "Severe", "Pain Type": "sharp", "Body Part": "legs", "Duration": "after last session", "Sentiment": "Negative"},
    {"Input Text": "There's a nagging pain in my back that comes and goes throughout the day.", "Cleaned Text": "nagging pain back come go throughout day", "Pain Intensity": "Moderate", "Pain Type": "nagging", "Body Part": "back", "Duration": "throughout the day", "Sentiment": "Negative"},
    {"Input Text": "I feel a sharp pain in my ribcage that gets worse when I cough.", "Cleaned Text": "sharp pain ribcage get worse cough", "Pain Intensity": "Severe", "Pain Type": "sharp", "Body Part": "ribcage", "Duration": "when coughing", "Sentiment": "Negative"},
    {"Input Text": "After treatment, I have a constant, dull pain in my back that doesn’t go away.", "Cleaned Text": "after treatment have constant dull pain back not go away", "Pain Intensity": "Moderate", "Pain Type": "dull", "Body Part": "back", "Duration": "after treatment", "Sentiment": "Negative"},
    {"Input Text": "I experience a shooting pain in my shoulder whenever I lift my arm.", "Cleaned Text": "experience shooting pain shoulder whenever lift arm", "Pain Intensity": "Severe", "Pain Type": "shooting", "Body Part": "shoulder", "Duration": "when lifting", "Sentiment": "Negative"},
    {"Input Text": "There's a dull ache in my lower back that has been persistent for weeks now.", "Cleaned Text": "dull ache lower back persistent week now", "Pain Intensity": "Moderate", "Pain Type": "dull", "Body Part": "lower back", "Duration": "for weeks", "Sentiment": "Negative"},
    {"Input Text": "I feel a sharp pain in my abdomen that makes it hard to move.", "Cleaned Text": "sharp pain abdomen make hard move", "Pain Intensity": "Severe", "Pain Type": "sharp", "Body Part": "abdomen", "Duration": "makes it hard to move", "Sentiment": "Negative"},
    {"Input Text": "After treatment, I have a constant throbbing pain in my head that never goes away.", "Cleaned Text": "after treatment have constant throbbing pain head never go away", "Pain Intensity": "Severe", "Pain Type": "throbbing", "Body Part": "head", "Duration": "constant", "Sentiment": "Negative"},
    {"Input Text": "There's a sharp pain in my lower back that feels like it's getting worse.", "Cleaned Text": "sharp pain lower back feel get worse", "Pain Intensity": "Severe", "Pain Type": "sharp", "Body Part": "lower back", "Duration": "feels like it's getting worse", "Sentiment": "Negative"},
    {"Input Text": "I experience dull pain in my neck that becomes worse when I look up.", "Cleaned Text": "experience dull pain neck worse look up", "Pain Intensity": "Moderate", "Pain Type": "dull", "Body Part": "neck", "Duration": "when looking up", "Sentiment": "Negative"},
    {"Input Text": "I have a burning pain in my stomach after eating, which is quite concerning.", "Cleaned Text": "burning pain stomach after eat quite concerning", "Pain Intensity": "Moderate", "Pain Type": "burning", "Body Part": "stomach", "Duration": "after eating", "Sentiment": "Negative"},
    {"Input Text": "I feel a throbbing pain in my legs after standing for a long time.", "Cleaned Text": "throbbing pain legs after standing long time", "Pain Intensity": "Moderate", "Pain Type": "throbbing", "Body Part": "legs", "Duration": "after standing", "Sentiment": "Negative"},
    {"Input Text": "After my last treatment, I have a constant pain in my left hip.", "Cleaned Text": "after last treatment have constant pain left hip", "Pain Intensity": "Moderate", "Pain Type": "pain", "Body Part": "left hip", "Duration": "after last treatment", "Sentiment": "Negative"},
    {"Input Text": "I have a sharp pain in my back that has been there for about two weeks.", "Cleaned Text": "sharp pain back been there about two week", "Pain Intensity": "Moderate", "Pain Type": "sharp", "Body Part": "back", "Duration": "for about two weeks", "Sentiment": "Negative"},
    {"Input Text": "There’s a dull pain in my hips that makes walking difficult.", "Cleaned Text": "dull pain hips make walk difficult", "Pain Intensity": "Moderate", "Pain Type": "dull", "Body Part": "hips", "Duration": "makes walking difficult", "Sentiment": "Negative"},
    {"Input Text": "I often feel a burning sensation in my throat, especially after eating spicy food.", "Cleaned Text": "often feel burning sensation throat especially after eat spicy food", "Pain Intensity": "Moderate", "Pain Type": "burning", "Body Part": "throat", "Duration": "after eating spicy food", "Sentiment": "Negative"},
    {"Input Text": "There's a sharp pain in my right knee that makes it hard to climb stairs.", "Cleaned Text": "sharp pain right knee make hard climb stairs", "Pain Intensity": "Moderate", "Pain Type": "sharp", "Body Part": "right knee", "Duration": "when climbing stairs", "Sentiment": "Negative"},
    {"Input Text": "I have a constant ache in my left leg that has been bothering me for weeks.", "Cleaned Text": "constant ache left leg bother weeks", "Pain Intensity": "Moderate", "Pain Type": "ache", "Body Part": "left leg", "Duration": "for weeks", "Sentiment": "Negative"},
    {"Input Text": "After chemotherapy, I have a shooting pain in my abdomen that worries me.", "Cleaned Text": "after chemotherapy have shooting pain abdomen worry", "Pain Intensity": "Severe", "Pain Type": "shooting", "Body Part": "abdomen", "Duration": "after chemotherapy", "Sentiment": "Negative"},
    {"Input Text": "I feel a constant throbbing pain in my foot that doesn't seem to subside.", "Cleaned Text": "constant throbbing pain foot not seem subside", "Pain Intensity": "Moderate", "Pain Type": "throbbing", "Body Part": "foot", "Duration": "constant", "Sentiment": "Negative"},
    {"Input Text": "There's a persistent sharp pain in my side that started after my last treatment.", "Cleaned Text": "persistent sharp pain side start after last treatment", "Pain Intensity": "Severe", "Pain Type": "sharp", "Body Part": "side", "Duration": "after last treatment", "Sentiment": "Negative"},
    {"Input Text": "I often experience a dull pain in my back that makes sitting uncomfortable.", "Cleaned Text": "often experience dull pain back make sitting uncomfortable", "Pain Intensity": "Moderate", "Pain Type": "dull", "Body Part": "back", "Duration": "when sitting", "Sentiment": "Negative"},
]

# Convert to DataFrame for better visualization and export if needed
df = pd.DataFrame(data_entries)

# merge with cancer_pain_data.csv
df = pd.concat([df, pd.read_csv('cancer_pain_data.csv')], ignore_index=True)

print(len(data) + len(data_entries) + len(additional_entries))
print(len(df))

df.to_csv('cancer_pain_data.csv', index=False)

print("concat done!")

# import csv
# # create a reader
# rd = csv.reader()