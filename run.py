import tensorflow as tf
import gym

from rl import A3CAgent, track
from util import *
from midi_util import *
import midi

samples = 5

with tf.device('/cpu:0'), tf.Session() as sess:
    agent = make_agent()
    agent.load(sess)

    env = track(gym.make('music-v0'))
    for sample_count in range(samples):
        agent.run(sess, env)
        print('Composition', env.composition)
        mf = midi_encode_melody(env.composition)
        midi.write_midifile('out/output.mid', mf)
