#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.2),
    on August 17, 2026, at 09:51
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.2'
expName = 'JDM'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'name': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1707, 1067]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['name'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='G:\\My Drive\\Teaching\\FA 26 PSY 30400\\Experiments\\JDM\\JDM_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color='white', colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = 'white'
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instructions" ---
    text_7 = visual.TextStim(win=win, name='text_7',
        text='On each trial, you will be given a prompt.\n\nSometimes, you will need to type in a response. Other times, you will choose between a set of options. Try to answer as quickly and accurately as possible.\n\nPress the spacebar to begin.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "crt_trial" ---
    text_4 = visual.TextStim(win=win, name='text_4',
        text='',
        font='Arial',
        pos=(0, .3), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    textbox = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         ori=0.0, pos=(0, -.2), draggable=False,      letterHeight=0.03,
         size=(0.5, 0.1), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox',
         depth=-1, autoLog=True,
    )
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    text_5 = visual.TextStim(win=win, name='text_5',
        text='Type your response then press ENTER to submit it.',
        font='Arial',
        pos=(0, -.4), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text_6 = visual.TextStim(win=win, name='text_6',
        text='',
        font='Arial',
        pos=(.3, -.2), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "blank250" ---
    text_11 = visual.TextStim(win=win, name='text_11',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "prob_trial" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text='',
        font='Arial',
        pos=(0, .3), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_3 = visual.TextStim(win=win, name='text_3',
        text='',
        font='Arial',
        pos=(0, .1), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    mouse_2 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_2.mouseClock = core.Clock()
    ans1_text = visual.TextStim(win=win, name='ans1_text',
        text='',
        font='Arial',
        pos=(0, -.1), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    ans2_text = visual.TextStim(win=win, name='ans2_text',
        text='',
        font='Arial',
        pos=(0, -.2), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    ans3_text = visual.TextStim(win=win, name='ans3_text',
        text='',
        font='Arial',
        pos=(0, -.3), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    text_10 = visual.TextStim(win=win, name='text_10',
        text='(click one option)',
        font='Arial',
        pos=(0, -.4), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    
    # --- Initialize components for Routine "blank250" ---
    text_11 = visual.TextStim(win=win, name='text_11',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "gl_trial" ---
    text = visual.TextStim(win=win, name='text',
        text='Given the two options shown below, which would you prefer?',
        font='Arial',
        pos=(0, .3), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    opt1_text = visual.TextStim(win=win, name='opt1_text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    opt2_text = visual.TextStim(win=win, name='opt2_text',
        text='',
        font='Arial',
        pos=(0, -.1), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    text_9 = visual.TextStim(win=win, name='text_9',
        text='(click one option)',
        font='Arial',
        pos=(0, -.4), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "blank250" ---
    text_11 = visual.TextStim(win=win, name='text_11',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "end_task" ---
    text_8 = visual.TextStim(win=win, name='text_8',
        text='That is the end of the task.',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "instructions" ---
    # create an object to store info about Routine instructions
    instructions = data.Routine(
        name='instructions',
        components=[text_7, key_resp_2],
    )
    instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_2
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # store start times for instructions
    instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions.tStart = globalClock.getTime(format='float')
    instructions.status = STARTED
    thisExp.addData('instructions.started', instructions.tStart)
    instructions.maxDuration = None
    # keep track of which components have finished
    instructionsComponents = instructions.components
    for thisComponent in instructions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions" ---
    instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        
        # if text_7 is starting this frame...
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            # update status
            text_7.status = STARTED
            text_7.setAutoDraw(True)
        
        # if text_7 is active this frame...
        if text_7.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions
    instructions.tStop = globalClock.getTime(format='float')
    instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions.stopped', instructions.tStop)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    crt_trials = data.TrialHandler2(
        name='crt_trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('crt_items.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(crt_trials)  # add the loop to the experiment
    thisCrt_trial = crt_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCrt_trial.rgb)
    if thisCrt_trial != None:
        for paramName in thisCrt_trial:
            globals()[paramName] = thisCrt_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisCrt_trial in crt_trials:
        currentLoop = crt_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisCrt_trial.rgb)
        if thisCrt_trial != None:
            for paramName in thisCrt_trial:
                globals()[paramName] = thisCrt_trial[paramName]
        
        # --- Prepare to start Routine "crt_trial" ---
        # create an object to store info about Routine crt_trial
        crt_trial = data.Routine(
            name='crt_trial',
            components=[text_4, textbox, key_resp, text_5, text_6],
        )
        crt_trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_4.setText(item)
        textbox.reset()
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        text_6.setText(unit)
        # store start times for crt_trial
        crt_trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        crt_trial.tStart = globalClock.getTime(format='float')
        crt_trial.status = STARTED
        thisExp.addData('crt_trial.started', crt_trial.tStart)
        crt_trial.maxDuration = None
        # keep track of which components have finished
        crt_trialComponents = crt_trial.components
        for thisComponent in crt_trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "crt_trial" ---
        # if trial has changed, end Routine now
        if isinstance(crt_trials, data.TrialHandler2) and thisCrt_trial.thisN != crt_trials.thisTrial.thisN:
            continueRoutine = False
        crt_trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_4* updates
            
            # if text_4 is starting this frame...
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.started')
                # update status
                text_4.status = STARTED
                text_4.setAutoDraw(True)
            
            # if text_4 is active this frame...
            if text_4.status == STARTED:
                # update params
                pass
            
            # *textbox* updates
            
            # if textbox is starting this frame...
            if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox.frameNStart = frameN  # exact frame index
                textbox.tStart = t  # local t and not account for scr refresh
                textbox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox.started')
                # update status
                textbox.status = STARTED
                textbox.setAutoDraw(True)
            
            # if textbox is active this frame...
            if textbox.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['return'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_5* updates
            
            # if text_5 is starting this frame...
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.started')
                # update status
                text_5.status = STARTED
                text_5.setAutoDraw(True)
            
            # if text_5 is active this frame...
            if text_5.status == STARTED:
                # update params
                pass
            
            # *text_6* updates
            
            # if text_6 is starting this frame...
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.started')
                # update status
                text_6.status = STARTED
                text_6.setAutoDraw(True)
            
            # if text_6 is active this frame...
            if text_6.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                crt_trial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crt_trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "crt_trial" ---
        for thisComponent in crt_trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for crt_trial
        crt_trial.tStop = globalClock.getTime(format='float')
        crt_trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('crt_trial.stopped', crt_trial.tStop)
        crt_trials.addData('textbox.text',textbox.text)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        crt_trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            crt_trials.addData('key_resp.rt', key_resp.rt)
            crt_trials.addData('key_resp.duration', key_resp.duration)
        # the Routine "crt_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank250" ---
        # create an object to store info about Routine blank250
        blank250 = data.Routine(
            name='blank250',
            components=[text_11],
        )
        blank250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank250
        blank250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank250.tStart = globalClock.getTime(format='float')
        blank250.status = STARTED
        thisExp.addData('blank250.started', blank250.tStart)
        blank250.maxDuration = None
        # keep track of which components have finished
        blank250Components = blank250.components
        for thisComponent in blank250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank250" ---
        # if trial has changed, end Routine now
        if isinstance(crt_trials, data.TrialHandler2) and thisCrt_trial.thisN != crt_trials.thisTrial.thisN:
            continueRoutine = False
        blank250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_11* updates
            
            # if text_11 is starting this frame...
            if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_11.frameNStart = frameN  # exact frame index
                text_11.tStart = t  # local t and not account for scr refresh
                text_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_11.started')
                # update status
                text_11.status = STARTED
                text_11.setAutoDraw(True)
            
            # if text_11 is active this frame...
            if text_11.status == STARTED:
                # update params
                pass
            
            # if text_11 is stopping this frame...
            if text_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_11.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    text_11.tStop = t  # not accounting for scr refresh
                    text_11.tStopRefresh = tThisFlipGlobal  # on global time
                    text_11.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_11.stopped')
                    # update status
                    text_11.status = FINISHED
                    text_11.setAutoDraw(False)
            # Run 'Each Frame' code from code_2
            if t > .25:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank250" ---
        for thisComponent in blank250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank250
        blank250.tStop = globalClock.getTime(format='float')
        blank250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank250.stopped', blank250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank250.maxDurationReached:
            routineTimer.addTime(-blank250.maxDuration)
        elif blank250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'crt_trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    prob_trials = data.TrialHandler2(
        name='prob_trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('jdm_questions.csv'), 
        seed=None, 
    )
    thisExp.addLoop(prob_trials)  # add the loop to the experiment
    thisProb_trial = prob_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisProb_trial.rgb)
    if thisProb_trial != None:
        for paramName in thisProb_trial:
            globals()[paramName] = thisProb_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisProb_trial in prob_trials:
        currentLoop = prob_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisProb_trial.rgb)
        if thisProb_trial != None:
            for paramName in thisProb_trial:
                globals()[paramName] = thisProb_trial[paramName]
        
        # --- Prepare to start Routine "prob_trial" ---
        # create an object to store info about Routine prob_trial
        prob_trial = data.Routine(
            name='prob_trial',
            components=[text_2, text_3, mouse_2, ans1_text, ans2_text, ans3_text, text_10],
        )
        prob_trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        text_2.setText(prompt_text)
        text_3.setText(question_text)
        # setup some python lists for storing info about the mouse_2
        mouse_2.clicked_name = []
        gotValidClick = False  # until a click is received
        ans1_text.setText(ans1)
        ans2_text.setText(ans2)
        ans3_text.setText(ans3)
        # store start times for prob_trial
        prob_trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        prob_trial.tStart = globalClock.getTime(format='float')
        prob_trial.status = STARTED
        thisExp.addData('prob_trial.started', prob_trial.tStart)
        prob_trial.maxDuration = None
        # keep track of which components have finished
        prob_trialComponents = prob_trial.components
        for thisComponent in prob_trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "prob_trial" ---
        # if trial has changed, end Routine now
        if isinstance(prob_trials, data.TrialHandler2) and thisProb_trial.thisN != prob_trials.thisTrial.thisN:
            continueRoutine = False
        prob_trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            # *mouse_2* updates
            
            # if mouse_2 is starting this frame...
            if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse_2.frameNStart = frameN  # exact frame index
                mouse_2.tStart = t  # local t and not account for scr refresh
                mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse_2.started', t)
                # update status
                mouse_2.status = STARTED
                mouse_2.mouseClock.reset()
                prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
            if mouse_2.status == STARTED:  # only update if started and not finished!
                buttons = mouse_2.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([ans1_text, ans2_text, ans3_text], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse_2):
                                gotValidClick = True
                                mouse_2.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouse_2.clicked_name.append(None)
                        if gotValidClick:  
                            continueRoutine = False  # end routine on response
            
            # *ans1_text* updates
            
            # if ans1_text is starting this frame...
            if ans1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ans1_text.frameNStart = frameN  # exact frame index
                ans1_text.tStart = t  # local t and not account for scr refresh
                ans1_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ans1_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ans1_text.started')
                # update status
                ans1_text.status = STARTED
                ans1_text.setAutoDraw(True)
            
            # if ans1_text is active this frame...
            if ans1_text.status == STARTED:
                # update params
                pass
            
            # *ans2_text* updates
            
            # if ans2_text is starting this frame...
            if ans2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ans2_text.frameNStart = frameN  # exact frame index
                ans2_text.tStart = t  # local t and not account for scr refresh
                ans2_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ans2_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ans2_text.started')
                # update status
                ans2_text.status = STARTED
                ans2_text.setAutoDraw(True)
            
            # if ans2_text is active this frame...
            if ans2_text.status == STARTED:
                # update params
                pass
            
            # *ans3_text* updates
            
            # if ans3_text is starting this frame...
            if ans3_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ans3_text.frameNStart = frameN  # exact frame index
                ans3_text.tStart = t  # local t and not account for scr refresh
                ans3_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ans3_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ans3_text.started')
                # update status
                ans3_text.status = STARTED
                ans3_text.setAutoDraw(True)
            
            # if ans3_text is active this frame...
            if ans3_text.status == STARTED:
                # update params
                pass
            
            # *text_10* updates
            
            # if text_10 is starting this frame...
            if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_10.frameNStart = frameN  # exact frame index
                text_10.tStart = t  # local t and not account for scr refresh
                text_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_10.started')
                # update status
                text_10.status = STARTED
                text_10.setAutoDraw(True)
            
            # if text_10 is active this frame...
            if text_10.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                prob_trial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in prob_trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "prob_trial" ---
        for thisComponent in prob_trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for prob_trial
        prob_trial.tStop = globalClock.getTime(format='float')
        prob_trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('prob_trial.stopped', prob_trial.tStop)
        # store data for prob_trials (TrialHandler)
        x, y = mouse_2.getPos()
        buttons = mouse_2.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            clickableList = environmenttools.getFromNames([ans1_text, ans2_text, ans3_text], namespace=locals())
            for obj in clickableList:
                # is this object clicked on?
                if obj.contains(mouse_2):
                    gotValidClick = True
                    mouse_2.clicked_name.append(obj.name)
            if not gotValidClick:
                mouse_2.clicked_name.append(None)
        prob_trials.addData('mouse_2.x', x)
        prob_trials.addData('mouse_2.y', y)
        prob_trials.addData('mouse_2.leftButton', buttons[0])
        prob_trials.addData('mouse_2.midButton', buttons[1])
        prob_trials.addData('mouse_2.rightButton', buttons[2])
        if len(mouse_2.clicked_name):
            prob_trials.addData('mouse_2.clicked_name', mouse_2.clicked_name[0])
        # the Routine "prob_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank250" ---
        # create an object to store info about Routine blank250
        blank250 = data.Routine(
            name='blank250',
            components=[text_11],
        )
        blank250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank250
        blank250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank250.tStart = globalClock.getTime(format='float')
        blank250.status = STARTED
        thisExp.addData('blank250.started', blank250.tStart)
        blank250.maxDuration = None
        # keep track of which components have finished
        blank250Components = blank250.components
        for thisComponent in blank250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank250" ---
        # if trial has changed, end Routine now
        if isinstance(prob_trials, data.TrialHandler2) and thisProb_trial.thisN != prob_trials.thisTrial.thisN:
            continueRoutine = False
        blank250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_11* updates
            
            # if text_11 is starting this frame...
            if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_11.frameNStart = frameN  # exact frame index
                text_11.tStart = t  # local t and not account for scr refresh
                text_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_11.started')
                # update status
                text_11.status = STARTED
                text_11.setAutoDraw(True)
            
            # if text_11 is active this frame...
            if text_11.status == STARTED:
                # update params
                pass
            
            # if text_11 is stopping this frame...
            if text_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_11.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    text_11.tStop = t  # not accounting for scr refresh
                    text_11.tStopRefresh = tThisFlipGlobal  # on global time
                    text_11.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_11.stopped')
                    # update status
                    text_11.status = FINISHED
                    text_11.setAutoDraw(False)
            # Run 'Each Frame' code from code_2
            if t > .25:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank250" ---
        for thisComponent in blank250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank250
        blank250.tStop = globalClock.getTime(format='float')
        blank250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank250.stopped', blank250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank250.maxDurationReached:
            routineTimer.addTime(-blank250.maxDuration)
        elif blank250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'prob_trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    gl_trials = data.TrialHandler2(
        name='gl_trials',
        nReps=1.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('gain_loss.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(gl_trials)  # add the loop to the experiment
    thisGl_trial = gl_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGl_trial.rgb)
    if thisGl_trial != None:
        for paramName in thisGl_trial:
            globals()[paramName] = thisGl_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisGl_trial in gl_trials:
        currentLoop = gl_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisGl_trial.rgb)
        if thisGl_trial != None:
            for paramName in thisGl_trial:
                globals()[paramName] = thisGl_trial[paramName]
        
        # --- Prepare to start Routine "gl_trial" ---
        # create an object to store info about Routine gl_trial
        gl_trial = data.Routine(
            name='gl_trial',
            components=[text, mouse, opt1_text, opt2_text, text_9],
        )
        gl_trial.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        opt1_text.setText(opt1)
        opt2_text.setText(opt2)
        # store start times for gl_trial
        gl_trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        gl_trial.tStart = globalClock.getTime(format='float')
        gl_trial.status = STARTED
        thisExp.addData('gl_trial.started', gl_trial.tStart)
        gl_trial.maxDuration = None
        # keep track of which components have finished
        gl_trialComponents = gl_trial.components
        for thisComponent in gl_trial.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "gl_trial" ---
        # if trial has changed, end Routine now
        if isinstance(gl_trials, data.TrialHandler2) and thisGl_trial.thisN != gl_trials.thisTrial.thisN:
            continueRoutine = False
        gl_trial.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([opt1_text, opt2_text], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        if not gotValidClick:
                            mouse.clicked_name.append(None)
                        if gotValidClick:  
                            continueRoutine = False  # end routine on response
            
            # *opt1_text* updates
            
            # if opt1_text is starting this frame...
            if opt1_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                opt1_text.frameNStart = frameN  # exact frame index
                opt1_text.tStart = t  # local t and not account for scr refresh
                opt1_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(opt1_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'opt1_text.started')
                # update status
                opt1_text.status = STARTED
                opt1_text.setAutoDraw(True)
            
            # if opt1_text is active this frame...
            if opt1_text.status == STARTED:
                # update params
                pass
            
            # *opt2_text* updates
            
            # if opt2_text is starting this frame...
            if opt2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                opt2_text.frameNStart = frameN  # exact frame index
                opt2_text.tStart = t  # local t and not account for scr refresh
                opt2_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(opt2_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'opt2_text.started')
                # update status
                opt2_text.status = STARTED
                opt2_text.setAutoDraw(True)
            
            # if opt2_text is active this frame...
            if opt2_text.status == STARTED:
                # update params
                pass
            
            # *text_9* updates
            
            # if text_9 is starting this frame...
            if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_9.frameNStart = frameN  # exact frame index
                text_9.tStart = t  # local t and not account for scr refresh
                text_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_9.started')
                # update status
                text_9.status = STARTED
                text_9.setAutoDraw(True)
            
            # if text_9 is active this frame...
            if text_9.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                gl_trial.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in gl_trial.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "gl_trial" ---
        for thisComponent in gl_trial.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for gl_trial
        gl_trial.tStop = globalClock.getTime(format='float')
        gl_trial.tStopRefresh = tThisFlipGlobal
        thisExp.addData('gl_trial.stopped', gl_trial.tStop)
        # store data for gl_trials (TrialHandler)
        x, y = mouse.getPos()
        buttons = mouse.getPressed()
        if sum(buttons):
            # check if the mouse was inside our 'clickable' objects
            gotValidClick = False
            clickableList = environmenttools.getFromNames([opt1_text, opt2_text], namespace=locals())
            for obj in clickableList:
                # is this object clicked on?
                if obj.contains(mouse):
                    gotValidClick = True
                    mouse.clicked_name.append(obj.name)
            if not gotValidClick:
                mouse.clicked_name.append(None)
        gl_trials.addData('mouse.x', x)
        gl_trials.addData('mouse.y', y)
        gl_trials.addData('mouse.leftButton', buttons[0])
        gl_trials.addData('mouse.midButton', buttons[1])
        gl_trials.addData('mouse.rightButton', buttons[2])
        if len(mouse.clicked_name):
            gl_trials.addData('mouse.clicked_name', mouse.clicked_name[0])
        # the Routine "gl_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank250" ---
        # create an object to store info about Routine blank250
        blank250 = data.Routine(
            name='blank250',
            components=[text_11],
        )
        blank250.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank250
        blank250.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank250.tStart = globalClock.getTime(format='float')
        blank250.status = STARTED
        thisExp.addData('blank250.started', blank250.tStart)
        blank250.maxDuration = None
        # keep track of which components have finished
        blank250Components = blank250.components
        for thisComponent in blank250.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank250" ---
        # if trial has changed, end Routine now
        if isinstance(gl_trials, data.TrialHandler2) and thisGl_trial.thisN != gl_trials.thisTrial.thisN:
            continueRoutine = False
        blank250.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.25:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_11* updates
            
            # if text_11 is starting this frame...
            if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_11.frameNStart = frameN  # exact frame index
                text_11.tStart = t  # local t and not account for scr refresh
                text_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_11.started')
                # update status
                text_11.status = STARTED
                text_11.setAutoDraw(True)
            
            # if text_11 is active this frame...
            if text_11.status == STARTED:
                # update params
                pass
            
            # if text_11 is stopping this frame...
            if text_11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_11.tStartRefresh + .25-frameTolerance:
                    # keep track of stop time/frame for later
                    text_11.tStop = t  # not accounting for scr refresh
                    text_11.tStopRefresh = tThisFlipGlobal  # on global time
                    text_11.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_11.stopped')
                    # update status
                    text_11.status = FINISHED
                    text_11.setAutoDraw(False)
            # Run 'Each Frame' code from code_2
            if t > .25:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank250.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank250.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank250" ---
        for thisComponent in blank250.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank250
        blank250.tStop = globalClock.getTime(format='float')
        blank250.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank250.stopped', blank250.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank250.maxDurationReached:
            routineTimer.addTime(-blank250.maxDuration)
        elif blank250.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.250000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'gl_trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "end_task" ---
    # create an object to store info about Routine end_task
    end_task = data.Routine(
        name='end_task',
        components=[text_8],
    )
    end_task.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for end_task
    end_task.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    end_task.tStart = globalClock.getTime(format='float')
    end_task.status = STARTED
    thisExp.addData('end_task.started', end_task.tStart)
    end_task.maxDuration = None
    # keep track of which components have finished
    end_taskComponents = end_task.components
    for thisComponent in end_task.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end_task" ---
    end_task.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        
        # if text_8 is starting this frame...
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_8.started')
            # update status
            text_8.status = STARTED
            text_8.setAutoDraw(True)
        
        # if text_8 is active this frame...
        if text_8.status == STARTED:
            # update params
            pass
        
        # if text_8 is stopping this frame...
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.tStopRefresh = tThisFlipGlobal  # on global time
                text_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_8.stopped')
                # update status
                text_8.status = FINISHED
                text_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            end_task.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_task.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end_task" ---
    for thisComponent in end_task.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for end_task
    end_task.tStop = globalClock.getTime(format='float')
    end_task.tStopRefresh = tThisFlipGlobal
    thisExp.addData('end_task.stopped', end_task.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if end_task.maxDurationReached:
        routineTimer.addTime(-end_task.maxDuration)
    elif end_task.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    thisExp.nextEntry()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
