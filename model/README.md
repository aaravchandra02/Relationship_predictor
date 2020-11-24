This folder contains the model part of the whole application mainly the ML odel that we have generated using the code:

```
import pickle
with open('brain.pkl', 'wb') as f:
    pickle.dump(clf, f)
```