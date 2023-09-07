from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
happiness = 100
health = 50
finances = 50
willpower = 50
call = 0
job = 0
points = 0

def ending0():
    t = '\n“Hey, Ross. Good to see you again,”\n“I know! It feels like it’s been so long since university ended,”\n“So, what’ve you been up to lately? Did you get a job yet?”'
    if job == 0:
        t += '\n“Nope. Same as before.\nIt’s not the best, what with my landlord refusing to let me extend the deadlines on my payments any longer… but I’ll manage.\nWorst case scenario, I move back in with my parents.”'
    elif job == 1:
        t += '\n“Actually, I did get one. It doesn’t pay much, not nearly as much as yours, but it hasn’t been bad so far,”\n“So, what do you do?”\n“...nothing important. I… don’t want to talk about it,”'
    else:
        t += '\n“So, I work with a certain organisation to make sure women have access to equal rights and employment throughout the country.\nWith what I’ve been through the past two years, it’s something that has a special significance to me,”\n“That’s great. Really. You seem so much happier now, honestly,”\n“Thanks, I guess,”'
    return t

def ending1():
    t = ''
    if points >= 4 and call == 2:
        t += '\n“Well… there’s been trials and tribulations, but I think I really am. There’s a certain energy to life I’ve never felt before,”\n“That’s amazing to hear, especially from you. I guess both of us have finally found our places,”\n"We stayed that night for hours, talking and laughing about everything we’d been through since university ended.\nIt felt so nice to finally be free of stress, financial troubles, and the shadow of unspoken inequalities,\nand to be able to just relax and enjoy myself with a friend. Honestly? It was all worth it."\n---\nThanks for playing!\nAnd, congratulations on achieving the best ending to Isabel’s story.\nYou could leave.\nBut there are other endings, if you still want to see them.'
    elif points <= -2 and call != 2:
        t += '\n“Not really. Life isn’t great and it doesn’t seem to be getting better.\nRight now, honestly, I’m regretting even moving out.\nWhat’s the point of anything? I can’t even get a job… maybe I should do what my mother did and settle for some loveless marriage.\nAt least I won’t have to worry about rent anymore,”\n“I guess it’s come to this, huh? I didn’t think you’d cave in like this,”\n“I didn’t either. I’m sorry,”\n"We went our separate ways early that night.\n---\nThanks for playing!\nBut… there may be better endings to Isabel’s story.\nYou could play it again.\nOr not.\nIt’s your choice.'
    else:
        t += '\n“I’m not sure. I don’t feel particularly happy, but I don’t feel that sad, either.\nEveryday is just… endless seas of grey, but I’m doing fine. Really,”\n“I’m sorry about that. Maybe I-”\n“Don’t be. Really, just don’t be. I’m fine where I am, and I can’t deny that it hurts it a little at times, but I’m fine,”\n"We stayed that night for as long as we had planned. There wasn’t much else to do."\n---\nThanks for playing\n! But… maybe there’s a better ending to Isabel’s story.\nLooks like the only way to find out, though, would be to play it again.'
    return t

def updateStats():
    return 'Happiness: {}   Health: {}   Finances: {}   Willpower: {}'.format(
        happiness, health, finances, willpower)

state = {
    'choice': 'rejection',
    'text': '2021 was the Year of Celebrating Singaporean Women.\nAnd while 2021 has long been over, the challenges faced by women still remain entrenched in our society.\nWe believe spreading awareness of these issues is the first step to any real change, which is why we launched justinian.io.',
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['choice']
        state['text'] = tinput(user_input)
    if state['choice'] == 'rejection':
        state['text'] = updateStats() + '\n\n' + state['text']
    return render_template('game.html', game_text=state['text'] or '')  # Initialize as empty string if None

@app.route('/reset', methods=['GET'])
def reset():
    global happiness, health, finances, willpower
    happiness = 100
    health = 100
    finances = 100
    willpower = 100
    state['text'] = updateStats() + '\n\n2021 was the Year of Celebrating Singaporean Women.\nAnd while 2021 has long been over, the challenges faced by women still remain entrenched in our society.\nWe believe spreading awareness of these issues is the first step to any real change, which is why we launched justinian.io.'
    state['choice'] = 'rejection'
    return redirect(url_for('index'))

def tinput(user_input):
    global points
    global call
    global job
    choice = state['choice']

    if user_input.lower() == 'reset': #reset
        global happiness, health, finances, willpower
        happiness = 50
        health = 100
        finances = 100
        willpower = 50
        state['text'] = updateStats() + '\n\n2021 was the Year of Celebrating Singaporean Women.\nAnd while 2021 has long been over, the challenges faced by women still remain entrenched in our society.\nWe believe spreading awareness of these issues is the first step to any real change, which is why we launched justinian.io.'
        state['choice'] = 'rejection'
        return 'Game has been reset.'
    
    if happiness == 0:
        state['choice'] = 'happinessEnding'
    
    if choice == 'happinessEnding':
        if job == 0:
            state['text'] = 'I can’t do this anymore.\nI can’t.\nI want to drown myself.\nMaybe I should.\nHow’d things get this bad? I… need someone to talk to.\nI’ll have to put job-searching, but I can’t fight my own mind any longer.'
        else:
            state['text'] = 'I can’t do this anymore.\nI can’t.\nI want to drown myself.\nMaybe I should.\nHow’d things get this bad? I… need someone to talk to.\nI’ll have to hold on for a while, but I can’t fight my own mind any longer.'
    
    if health == 0:
        state['choice'] = 'healthEnding'
    
    if choice == 'healthEnding':
        state['text'] = '“My head… what happened?”\n“You collapsed halfway through a call with your friend, who helped bring you here. How long has your… condition… been like this?”\n“I… don’t know. I guess I’ve been really stressed lately, and I’ve taken… things… to cope, but I didn’t know things were this bad…”\n“Well, they are. You’re going to need to be here for another few months. I’m sorry, but… there isn’t any other option in this,”\n“...alright. I understand.”'

    if finances == 0:
        state['choice'] = 'financesEnding'
    
    if choice == 'financesEnding':
        state['text'] = '“Isabel? Isabel? Are you in there?”\n“Hey,”\n“Isabel? What’re you doing here? This place is a mess. You haven’t been answering my calls for days on end… this bedroom is full of food… have you done anything in weeks?”\n“I gave up,”\n“You gave up? But you were so determined! That night, as we left university-”\n“I gave up, Ross! It’s pointless! I’ve wasted two years on looking for a job, a lot more on getting those useless degrees, and so many more believing in myself,”\n“Isabel, please. I can’t bear to see you like this. You could at least-”\n“No. I’m happy where I am, I assure you… I’ll be moving back in with my parents soon, anyways. No point making the place look nice,”\n“Are you sure you’re happy? Please?”\n“I… you… I… you know what, I don’t want to deal with this. With you. Kindly get out of my house,”\n“Isabel, please-”\n“I said, get out of my house,”\n“Alright, Isabel. I hope you find happiness. I really do,”'

    if willpower == 0:
        state['choice'] = 'willpowerEnding'
    
    if choice == 'willpowerEnding':
        state['text'] = '“Father? Mother? It went as well as you thought it would,”\n“We told you, didn’t we? It’s alright, dear. We still love you. You can still be here. Just… help out with the chores, that’s all we’re asking,”\n“Thanks. For taking me in despite everything,”\n“It’s okay. Family is all you need,”\nThis was never what I imagined, but I guess it’s back to relying on my parents… again. I’ve wasted years on education for this? Oh well, it’s no-one’s fault but my own…'

    if choice == 'rejection': #initial case, displays reset text
        state['choice'] = 'rejectionOutcome'
        state['text'] = updateStats() + '\n“Hey, Isabel,” Ross called.\n“How’d the job application go? I know you really wanted this,”\n“Hi. About that… I didn’t get the job. Definitely hurts a little,”\n“Oh, that’s… disappointing. Are you alright?”\n“...”\n---\na: try again.\nb: "It was yet another failure."'
        return updateStats() + '\n“Hey, Isabel,” Ross called.\n“How’d the job application go? I know you really wanted this,”\n“Hi. About that… I didn’t get the job. Definitely hurts a little,”\n“Oh, that’s… disappointing. Are you alright?”\n“...”\n---\na: try again.\nb: "It was yet another failure."'

    elif choice == 'rejectionOutcome':
        if user_input.lower() == 'a':
            health -= 10
            happiness -= 10
            points += 1
            state['choice'] = 'whatWentWrong'
            state['text'] = updateStats() + '\nSo maybe it didn’t go my way this time.\nWell, it’s a setback, and a hard-hitting one at that, but it’s only temporary.\nI’m going to give myself a day or two to recover.\nLie on the couch, eat ice cream, watch that movie I missed.\nIt’ll be fun. Then, back into the swing of things.”'
            return updateStats() + '\nSo maybe it didn’t go my way this time.\nWell, it’s a setback, and a hard-hitting one at that, but it’s only temporary.\nI’m going to give myself a day or two to recover.\nLie on the couch, eat ice cream, watch that movie I missed.\nIt’ll be fun. Then, back into the swing of things.”'
        elif user_input.lower() == 'b':
            health -= 10
            points -= 1
            state['choice'] = 'whatWentWrong'
            state['text'] = updateStats() + '\n“It went just how I expected. Terribly. I need a break.\nI can’t deal with this right now. I just… can’t be around anything reminding me of the past 2 hours for a while.\nAnd by a while, I mean however long it takes me to forget.”'
            return updateStats() + '\n“It went just how I expected. Terribly. I need a break.\nI can’t deal with this right now. I just… can’t be around anything reminding me of the past 2 hours for a while.\nAnd by a while, I mean however long it takes me to forget.”'
        else:
            return 'invalid input'

    elif choice == 'whatWentWrong':
        state['choice'] = 'whatWentWrongOutcome'
        state['text'] = updateStats() + '\n“I have to examine the situation.\nSo far, it’s been looking like the biggest issue was my résumé, so I might want to deal with that somehow…”\n---\na: rewrite everything\nb: make small edits\nc: just leave it be'
        return updateStats() + '\n“I have to examine the situation.\nSo far, it’s been looking like the biggest issue was my résumé, so I might want to deal with that somehow…”\n---\na: rewrite everything\nb: make small edits\nc: just leave it be'
    
    elif choice == 'whatWentWrongOutcome':
        if user_input.lower() == 'a':
            willpower -= 10
            points += 1
            state['choice'] = 'theDiscussion'
            state['text'] = updateStats() + '\nAlright, after a few hours… or days, more like… of watching tutorials and seeking advice,\nit’s time to finally work on this. This won’t be easy, or fun, but it’ll help in the long run.\nI know it.'
            return updateStats() + '\nAlright, after a few hours… or days, more like… of watching tutorials and seeking advice,\nit’s time to finally work on this. This won’t be easy, or fun, but it’ll help in the long run.\nI know it.'
        elif user_input.lower() == 'b':
            state['choice'] = 'theDiscussion'
            state['text'] = updateStats() + '\nNo way I’m going to do a full rewrite. Not right now.\nLook, I can just… edit a few bits to make it look nicer… maybe get ChatGPT to write this bit for me…\nI just want a while to sit quietly in the corner and cry.'
            return updateStats() + '\nNo way I’m going to do a full rewrite. Not right now.\nLook, I can just… edit a few bits to make it look nicer… maybe get ChatGPT to write this bit for me…\nI just want a while to sit quietly in the corner and cry.'
        elif user_input.lower() == 'c':
            happiness += 30
            health -= 10
            points -= 1
            state['choice'] = 'theDiscussion'
            state['text'] = updateStats() + '\nI can’t… I can’t deal with this. Any of this. I give up.\nWhat am I even meant to do in this situation?\nAnd by that, I mean… where’s that bottle I was saving?'
            return updateStats() + '\nI can’t… I can’t deal with this. Any of this. I give up.\nWhat am I even meant to do in this situation?\nAnd by that, I mean… where’s that bottle I was saving?'
        else:
            return 'invalid input'
    
    elif choice == 'theDiscussion':
        state['choice'] = 'theDiscussionOutcome'
        state['text'] = updateStats() + '\nRoss’s application went through, it seems.\nGuess I’ll call him and ask how it went.\nIt’s only fair, given that he did the same for me.\n---\na: "Good for him, I guess..."\nb: "Of course he got in."'
        return updateStats() + '\nRoss’s application went through, it seems.\nGuess I’ll call him and ask how it went.\nIt’s only fair, given that he did the same for me.\n---\na: "Good for him, I guess..."\nb: "Of course he got in."'
    
    elif choice == 'theDiscussionOutcome':
        if user_input.lower() == 'a':
            willpower -= 10
            happiness -= 10
            points += 1
            state['choice'] = 'againstTheOdds'
            state['text'] = updateStats() + '\nSo Ross got in? Great.\nSure, it stings a little, but I can still be happy for a friend, right?\nThough I have to wonder if the judgement might have been somewhat unfair…'
            return updateStats() + '\nSo Ross got in? Great.\nSure, it stings a little, but I can still be happy for a friend, right?\nThough I have to wonder if the judgement might have been somewhat unfair…'
        elif user_input.lower() == 'b':
            happiness += 10
            points -= 1
            state['choice'] = 'againstTheOdds'
            state['text'] = updateStats() + '\nSo Ross got in.\nIs anyone really surprised? He’s smart, charismatic, tall, and most importantly,\nhe’s the gender they’re looking for. Why do I even try, really, when all the odds are stacked against me?\nI hate this. I hate his stupid face. His texts can wait, I have a show to watch…'
            return updateStats() + '\nSo Ross got in.\nIs anyone really surprised? He’s smart, charismatic, tall, and most importantly,\nhe’s the gender they’re looking for. Why do I even try, really, when all the odds are stacked against me?\nI hate this. I hate his stupid face. His texts can wait, I have a show to watch…'
        else:
            return 'invalid input'
        
    elif choice == 'againstTheOdds':
        state['choice'] = 'againstTheOddsOutcome'
        state['text'] = updateStats() + '\nIt hasn’t been easy, but maybe there are some people\nthat could help me make sure my gender isn’t a disadvantage.\n---\na: Reach out for help\nb: Admit defeat'
        return updateStats() + '\nIt hasn’t been easy, but maybe there are some people\nthat could help me make sure my gender isn’t a disadvantage.\n---\na: Reach out for help\nb: Admit defeat'
    
    elif choice == 'againstTheOddsOutcome':
        if user_input.lower() == 'a':
            call = 1
            willpower -= 10
            points += 1
            state['choice'] = 'aSecondOpportunity'
            state['text'] = updateStats() + '\nI know it might be a long shot, but I can’t help but feel like I didn’t get the job because of my gender.\nMaybe I should make that call I’ve been putting off.'
            return updateStats() + '\nI know it might be a long shot, but I can’t help but feel like I didn’t get the job because of my gender.\nMaybe I should make that call I’ve been putting off.'
        elif user_input.lower() == 'b':
            happiness += 10
            points -= 2
            state['choice'] = 'aSecondOpportunity'
            state['text'] = updateStats() + '\nWhat’s the point? I lost. That’s it. Gender equality or inequality can wait.\nAll I want right now is a new bottle, and then… I’ll cross that bridge when I get there.'
            return updateStats() + '\nWhat’s the point? I lost. That’s it. Gender equality or inequality can wait.\nAll I want right now is a new bottle, and then… I’ll cross that bridge when I get there.'
        else:
            return 'invalid input'
    
    elif choice == 'aSecondOpportunity':
        state['choice'] = 'aSecondOpportunityOutcome'
        state['text'] = updateStats() + '\nOne of my applications succeeded! I can’t believe it!\nIt hardly pays as much as I’d like, but maybe I should take it… or I could continue searching.\nEither way, I don’t have infinite energy, and I’ll have to focus on either searching for a job or working at one.\n---\na: continue the search\nb: take the offer'
        return updateStats() + '\nOne of my applications succeeded! I can’t believe it!\nIt hardly pays as much as I’d like, but maybe I should take it… or I could continue searching.\nEither way, I don’t have infinite energy, and I’ll have to focus on either searching for a job or working at one.\n---\na: continue the search\nb: take the offer'
    
    elif choice == 'aSecondOpportunityOutcome':
        if user_input.lower() == 'a':
            willpower -= 10
            state['choice'] = 'statusQuo'
            if call == 1:
                state['choice'] = 'theCall'
                call = 2
            points += 1
            state['text'] = updateStats() + '\nWe’re not done yet.\nThere’s so much more that I could do, and I definitely can’t just stop now.\nThe search will go on for as long as I can sustain it.'
            return updateStats() + '\nWe’re not done yet.\nThere’s so much more that I could do, and I definitely can’t just stop now.\nThe search will go on for as long as I can sustain it.'
        elif user_input.lower() == 'b':
            job = 1
            happiness += 10
            state['choice'] = 'statusQuo'
            state['text'] = updateStats() + '\nThis hurts a little, considering I worked for years to get a lot of qualifications,\nand now I’m not going to use any of them.\nOh well… I have work to do, and humiliating as it is, I really need the money.'
            return updateStats() + '\nThis hurts a little, considering I worked for years to get a lot of qualifications,\nand now I’m not going to use any of them.\nOh well… I have work to do, and humiliating as it is, I really need the money.'
        else:
            return 'invalid input'
    
    elif choice == "theCall":
        state['choice'] = 'theCallOutcome'
        state['text'] = updateStats() + '\n“You’re Isabel, right?”\n“Yes,”\n“We might have an offer for you.\nI can’t promise it’ll pay much, but I think you really do care about this cause.\nBesides, you do have a lot of the media-oriented skills we need."\n---\na: accept\nb: decline'
        return updateStats() + '\n“You’re Isabel, right?”\n“Yes,”\n“We might have an offer for you.\nI can’t promise it’ll pay much, but I think you really do care about this cause.\nBesides, you do have a lot of the media-oriented skills we need."\n---\na: accept\nb: decline'

    elif choice == 'theCallOutcome':
        if user_input.lower() == 'a':
            job = 2
            points += 1
            state['choice'] = 'aNightInTheCity'
            state['text'] = updateStats() + '\n“Of course! What you’re doing is wonderful, and I’d be happy to help with your campaign.”'
            return updateStats() + '\n“Of course! What you’re doing is wonderful, and I’d be happy to help with your campaign.”'
        elif user_input.lower() == 'b':
            willpower += 10
            state['choice'] = 'statusQuo'
            state['text'] = updateStats() + '\n“Sorry, I… can’t bring myself to do this right now. I just don’t have the time.”'
            return updateStats() + '\n“Sorry, I… can’t bring myself to do this right now. I just don’t have the time.”'
        else:
            return 'invalid input'
    
    elif choice == 'statusQuo':
        state['choice'] = 'aNightInTheCity'
        state['text'] = updateStats() + '\nWe’re back here again.\nJobless once more.\nTime to continue applying, I suppose…'
    
    elif choice == 'aNightInTheCity':
        textOut = ending0()
        state['choice'] = 'night1'
        state['text'] = textOut
        return render_template('game.html', game_text=textOut)

    elif choice == 'night1':
        textOut = '\n“And, one more thing. Are you… happy?”'
        state['choice'] = 'night2'
        state['text'] = textOut
        return render_template('game.html', game_text=textOut)
    
    elif choice == 'night2':
        textOut = ending1()
        state ['choice'] = 'night2'
        state['text'] = textOut
        return render_template('game.html', game_text=textOut)

    else:
        state['text'] = 'invalid'
        return 'invalid input'

if __name__ == '__main__':
    app.run(debug=True)


