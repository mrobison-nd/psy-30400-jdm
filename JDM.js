/************ 
 * Jdm *
 ************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.2.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'JDM';  // from the Builder filename that created this script
let expInfo = {
    'name': '',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('white'),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
const crt_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(crt_trialsLoopBegin(crt_trialsLoopScheduler));
flowScheduler.add(crt_trialsLoopScheduler);
flowScheduler.add(crt_trialsLoopEnd);



const prob_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prob_trialsLoopBegin(prob_trialsLoopScheduler));
flowScheduler.add(prob_trialsLoopScheduler);
flowScheduler.add(prob_trialsLoopEnd);



const gl_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(gl_trialsLoopBegin(gl_trialsLoopScheduler));
flowScheduler.add(gl_trialsLoopScheduler);
flowScheduler.add(gl_trialsLoopEnd);



flowScheduler.add(end_taskRoutineBegin());
flowScheduler.add(end_taskRoutineEachFrame());
flowScheduler.add(end_taskRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'crt_items.xlsx', 'path': 'crt_items.xlsx'},
    {'name': 'jdm_questions.csv', 'path': 'jdm_questions.csv'},
    {'name': 'gain_loss.xlsx', 'path': 'gain_loss.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.2';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["name"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var instructionsClock;
var text_7;
var key_resp_2;
var crt_trialClock;
var text_4;
var textbox;
var key_resp;
var text_5;
var text_6;
var blank250Clock;
var text_11;
var prob_trialClock;
var text_2;
var text_3;
var mouse_2;
var ans1_text;
var ans2_text;
var ans3_text;
var text_10;
var gl_trialClock;
var text;
var mouse;
var opt1_text;
var opt2_text;
var text_9;
var end_taskClock;
var text_8;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'On each trial, you will be given a prompt.\n\nSometimes, you will need to type in a response. Other times, you will choose between a set of options. Try to answer as quickly and accurately as possible.\n\nPress the spacebar to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "crt_trial"
  crt_trialClock = new util.Clock();
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  textbox = new visual.TextBox({
    win: psychoJS.window,
    name: 'textbox',
    text: '',
    placeholder: 'Type here...',
    font: 'Arial',
    pos: [0, (- 0.2)], 
    draggable: false,
    letterHeight: 0.03,
    lineSpacing: 1.0,
    size: [0.5, 0.1],  units: undefined, 
    ori: 0.0,
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: 'black',
    languageStyle: 'LTR',
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    alignment: 'center',
    overflow: 'visible',
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'Type your response then press ENTER to submit it.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0.3, (- 0.2)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "blank250"
  blank250Clock = new util.Clock();
  text_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_11',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "prob_trial"
  prob_trialClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  mouse_2 = new core.Mouse({
    win: psychoJS.window,
  });
  mouse_2.mouseClock = new util.Clock();
  ans1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'ans1_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.1)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  ans2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'ans2_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  ans3_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'ans3_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: '(click one option)',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  // Initialize components for Routine "gl_trial"
  gl_trialClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Given the two options shown below, which would you prefer?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  opt1_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'opt1_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  opt2_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'opt2_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.1)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: '(click one option)',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "end_task"
  end_taskClock = new util.Clock();
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: 'That is the end of the task.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var instructionsMaxDurationReached;
var _key_resp_2_allKeys;
var instructionsMaxDuration;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    instructionsMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    psychoJS.experiment.addData('instructions.started', globalClock.getTime());
    instructionsMaxDuration = null
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(text_7);
    instructionsComponents.push(key_resp_2);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('instructions.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var crt_trials;
function crt_trialsLoopBegin(crt_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    crt_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'crt_items.xlsx',
      seed: undefined, name: 'crt_trials'
    });
    psychoJS.experiment.addLoop(crt_trials); // add the loop to the experiment
    currentLoop = crt_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCrt_trial of crt_trials) {
      snapshot = crt_trials.getSnapshot();
      crt_trialsLoopScheduler.add(importConditions(snapshot));
      crt_trialsLoopScheduler.add(crt_trialRoutineBegin(snapshot));
      crt_trialsLoopScheduler.add(crt_trialRoutineEachFrame());
      crt_trialsLoopScheduler.add(crt_trialRoutineEnd(snapshot));
      crt_trialsLoopScheduler.add(blank250RoutineBegin(snapshot));
      crt_trialsLoopScheduler.add(blank250RoutineEachFrame());
      crt_trialsLoopScheduler.add(blank250RoutineEnd(snapshot));
      crt_trialsLoopScheduler.add(crt_trialsLoopEndIteration(crt_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function crt_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(crt_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function crt_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var prob_trials;
function prob_trialsLoopBegin(prob_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prob_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'jdm_questions.csv',
      seed: undefined, name: 'prob_trials'
    });
    psychoJS.experiment.addLoop(prob_trials); // add the loop to the experiment
    currentLoop = prob_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisProb_trial of prob_trials) {
      snapshot = prob_trials.getSnapshot();
      prob_trialsLoopScheduler.add(importConditions(snapshot));
      prob_trialsLoopScheduler.add(prob_trialRoutineBegin(snapshot));
      prob_trialsLoopScheduler.add(prob_trialRoutineEachFrame());
      prob_trialsLoopScheduler.add(prob_trialRoutineEnd(snapshot));
      prob_trialsLoopScheduler.add(blank250RoutineBegin(snapshot));
      prob_trialsLoopScheduler.add(blank250RoutineEachFrame());
      prob_trialsLoopScheduler.add(blank250RoutineEnd(snapshot));
      prob_trialsLoopScheduler.add(prob_trialsLoopEndIteration(prob_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function prob_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(prob_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function prob_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var gl_trials;
function gl_trialsLoopBegin(gl_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    gl_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'gain_loss.xlsx',
      seed: undefined, name: 'gl_trials'
    });
    psychoJS.experiment.addLoop(gl_trials); // add the loop to the experiment
    currentLoop = gl_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisGl_trial of gl_trials) {
      snapshot = gl_trials.getSnapshot();
      gl_trialsLoopScheduler.add(importConditions(snapshot));
      gl_trialsLoopScheduler.add(gl_trialRoutineBegin(snapshot));
      gl_trialsLoopScheduler.add(gl_trialRoutineEachFrame());
      gl_trialsLoopScheduler.add(gl_trialRoutineEnd(snapshot));
      gl_trialsLoopScheduler.add(blank250RoutineBegin(snapshot));
      gl_trialsLoopScheduler.add(blank250RoutineEachFrame());
      gl_trialsLoopScheduler.add(blank250RoutineEnd(snapshot));
      gl_trialsLoopScheduler.add(gl_trialsLoopEndIteration(gl_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function gl_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(gl_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function gl_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var crt_trialMaxDurationReached;
var _key_resp_allKeys;
var crt_trialMaxDuration;
var crt_trialComponents;
function crt_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'crt_trial' ---
    t = 0;
    crt_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    crt_trialMaxDurationReached = false;
    // update component parameters for each repeat
    text_4.setText(item);
    textbox.setText('');
    textbox.refresh();
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    text_6.setText(unit);
    psychoJS.experiment.addData('crt_trial.started', globalClock.getTime());
    crt_trialMaxDuration = null
    // keep track of which components have finished
    crt_trialComponents = [];
    crt_trialComponents.push(text_4);
    crt_trialComponents.push(textbox);
    crt_trialComponents.push(key_resp);
    crt_trialComponents.push(text_5);
    crt_trialComponents.push(text_6);
    
    for (const thisComponent of crt_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function crt_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'crt_trial' ---
    // get current time
    t = crt_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    
    // *textbox* updates
    if (t >= 0.0 && textbox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textbox.tStart = t;  // (not accounting for frame time here)
      textbox.frameNStart = frameN;  // exact frame index
      
      textbox.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['return'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }
    
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of crt_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function crt_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'crt_trial' ---
    for (const thisComponent of crt_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('crt_trial.stopped', globalClock.getTime());
    psychoJS.experiment.addData('textbox.text',textbox.text)
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "crt_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var blank250MaxDurationReached;
var blank250MaxDuration;
var blank250Components;
function blank250RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blank250' ---
    t = 0;
    blank250Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.250000);
    blank250MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('blank250.started', globalClock.getTime());
    blank250MaxDuration = null
    // keep track of which components have finished
    blank250Components = [];
    blank250Components.push(text_11);
    
    for (const thisComponent of blank250Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function blank250RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blank250' ---
    // get current time
    t = blank250Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_11* updates
    if (t >= 0.0 && text_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_11.tStart = t;  // (not accounting for frame time here)
      text_11.frameNStart = frameN;  // exact frame index
      
      text_11.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_11.setAutoDraw(false);
    }
    
    // Run 'Each Frame' code from code_2
    if ((t > 0.25)) {
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of blank250Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function blank250RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blank250' ---
    for (const thisComponent of blank250Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('blank250.stopped', globalClock.getTime());
    if (blank250MaxDurationReached) {
        routineTimer.add(blank250MaxDuration);
    } else {
        routineTimer.add(-0.250000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var prob_trialMaxDurationReached;
var gotValidClick;
var prob_trialMaxDuration;
var prob_trialComponents;
function prob_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prob_trial' ---
    t = 0;
    prob_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    prob_trialMaxDurationReached = false;
    // update component parameters for each repeat
    text_2.setText(prompt_text);
    text_3.setText(question_text);
    // setup some python lists for storing info about the mouse_2
    mouse_2.clicked_name = [];
    gotValidClick = false; // until a click is received
    ans1_text.setText(ans1);
    ans2_text.setText(ans2);
    ans3_text.setText(ans3);
    psychoJS.experiment.addData('prob_trial.started', globalClock.getTime());
    prob_trialMaxDuration = null
    // keep track of which components have finished
    prob_trialComponents = [];
    prob_trialComponents.push(text_2);
    prob_trialComponents.push(text_3);
    prob_trialComponents.push(mouse_2);
    prob_trialComponents.push(ans1_text);
    prob_trialComponents.push(ans2_text);
    prob_trialComponents.push(ans3_text);
    prob_trialComponents.push(text_10);
    
    for (const thisComponent of prob_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
function prob_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prob_trial' ---
    // get current time
    t = prob_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    // *mouse_2* updates
    if (t >= 0.0 && mouse_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse_2.tStart = t;  // (not accounting for frame time here)
      mouse_2.frameNStart = frameN;  // exact frame index
      
      mouse_2.status = PsychoJS.Status.STARTED;
      mouse_2.mouseClock.reset();
      prevButtonState = mouse_2.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse_2.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse_2.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse_2.clickableObjects = eval([ans1_text, ans2_text, ans3_text])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse_2.clickableObjects)) {
              mouse_2.clickableObjects = [mouse_2.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse_2.clickableObjects) {
              if (obj.contains(mouse_2)) {
                  gotValidClick = true;
                  mouse_2.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              mouse_2.clicked_name.push(null);
          }
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *ans1_text* updates
    if (t >= 0.0 && ans1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans1_text.tStart = t;  // (not accounting for frame time here)
      ans1_text.frameNStart = frameN;  // exact frame index
      
      ans1_text.setAutoDraw(true);
    }
    
    
    // *ans2_text* updates
    if (t >= 0.0 && ans2_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans2_text.tStart = t;  // (not accounting for frame time here)
      ans2_text.frameNStart = frameN;  // exact frame index
      
      ans2_text.setAutoDraw(true);
    }
    
    
    // *ans3_text* updates
    if (t >= 0.0 && ans3_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ans3_text.tStart = t;  // (not accounting for frame time here)
      ans3_text.frameNStart = frameN;  // exact frame index
      
      ans3_text.setAutoDraw(true);
    }
    
    
    // *text_10* updates
    if (t >= 0.0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_10.tStart = t;  // (not accounting for frame time here)
      text_10.frameNStart = frameN;  // exact frame index
      
      text_10.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of prob_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var _mouseXYs;
function prob_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prob_trial' ---
    for (const thisComponent of prob_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('prob_trial.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse_2.getPos();
    _mouseButtons = mouse_2.getPressed();
    psychoJS.experiment.addData('mouse_2.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse_2.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse_2.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse_2.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse_2.rightButton', _mouseButtons[2]);
    if (mouse_2.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse_2.clicked_name', mouse_2.clicked_name[0]);}
    // the Routine "prob_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var gl_trialMaxDurationReached;
var gl_trialMaxDuration;
var gl_trialComponents;
function gl_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'gl_trial' ---
    t = 0;
    gl_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    gl_trialMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse
    mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    opt1_text.setText(opt1);
    opt2_text.setText(opt2);
    psychoJS.experiment.addData('gl_trial.started', globalClock.getTime());
    gl_trialMaxDuration = null
    // keep track of which components have finished
    gl_trialComponents = [];
    gl_trialComponents.push(text);
    gl_trialComponents.push(mouse);
    gl_trialComponents.push(opt1_text);
    gl_trialComponents.push(opt2_text);
    gl_trialComponents.push(text_9);
    
    for (const thisComponent of gl_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function gl_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'gl_trial' ---
    // get current time
    t = gl_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    // *mouse* updates
    if (t >= 0.0 && mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      mouse.tStart = t;  // (not accounting for frame time here)
      mouse.frameNStart = frameN;  // exact frame index
      
      mouse.status = PsychoJS.Status.STARTED;
      mouse.mouseClock.reset();
      prevButtonState = mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          mouse.clickableObjects = eval([opt1_text, opt2_text])
          ;// make sure the mouse's clickable objects are an array
          if (!Array.isArray(mouse.clickableObjects)) {
              mouse.clickableObjects = [mouse.clickableObjects];
          }
          // iterate through clickable objects and check each
          for (const obj of mouse.clickableObjects) {
              if (obj.contains(mouse)) {
                  gotValidClick = true;
                  mouse.clicked_name.push(obj.name);
              }
          }
          if (!gotValidClick) {
              mouse.clicked_name.push(null);
          }
          if (gotValidClick === true) { // end routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *opt1_text* updates
    if (t >= 0.0 && opt1_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      opt1_text.tStart = t;  // (not accounting for frame time here)
      opt1_text.frameNStart = frameN;  // exact frame index
      
      opt1_text.setAutoDraw(true);
    }
    
    
    // *opt2_text* updates
    if (t >= 0.0 && opt2_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      opt2_text.tStart = t;  // (not accounting for frame time here)
      opt2_text.frameNStart = frameN;  // exact frame index
      
      opt2_text.setAutoDraw(true);
    }
    
    
    // *text_9* updates
    if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index
      
      text_9.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of gl_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function gl_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'gl_trial' ---
    for (const thisComponent of gl_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('gl_trial.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse.getPos();
    _mouseButtons = mouse.getPressed();
    psychoJS.experiment.addData('mouse.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse.rightButton', _mouseButtons[2]);
    if (mouse.clicked_name.length > 0) {
      psychoJS.experiment.addData('mouse.clicked_name', mouse.clicked_name[0]);}
    // the Routine "gl_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var end_taskMaxDurationReached;
var end_taskMaxDuration;
var end_taskComponents;
function end_taskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end_task' ---
    t = 0;
    end_taskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    end_taskMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('end_task.started', globalClock.getTime());
    end_taskMaxDuration = null
    // keep track of which components have finished
    end_taskComponents = [];
    end_taskComponents.push(text_8);
    
    for (const thisComponent of end_taskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function end_taskRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_task' ---
    // get current time
    t = end_taskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_8* updates
    if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_8.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of end_taskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_taskRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_task' ---
    for (const thisComponent of end_taskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('end_task.stopped', globalClock.getTime());
    if (end_taskMaxDurationReached) {
        routineTimer.add(end_taskMaxDuration);
    } else {
        routineTimer.add(-3.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
