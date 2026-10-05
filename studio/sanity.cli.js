import {defineCliConfig} from 'sanity/cli'
import {PROJECT_ID, DATASET} from './project'

export default defineCliConfig({
  api: {projectId: PROJECT_ID, dataset: DATASET},
  // the editor's web address: https://blueprint-env.sanity.studio (change if taken)
  studioHost: 'blueprint-env',
  deployment: {autoUpdates: true},
})
