function centroids = computeCentroids(X, idx, K)

    [m n] = size(X);

    centroids = zeros(K, n);

    for i = 1:K

        ci = idx==i;

        ni = sum(ci);

        ci_matrix = repmat(ci, 1, n);

        centroids(i, :) = sum(X .* ci_matrix) ./ ni;

    end

end
function idx = findClosestCentroids(X, centroids)

    K = size(centroids, 1);

    idx = zeros(size(X, 1), 1);



    for i = 1:size(X, 1)

        index = zeros(1, K);

        for j = 1:K

            index(1, j) = sqrt(sum(power((X(i, :) - centroids(j, :)), 2)));

        end

        [d, id] = min(index);

        idx(i, 1) = id;

    end

end

function centroids = kMeansInitCentroids(X, K)

centroids = zeros(K, size(X, 2));



randidx = randperm(size(X, 1));

centroids = X(randidx(1:K), :);

end


[m n] = size(X);

K = size(initial_centroids, 1);

centroids = initial_centroids;

previous_centroids = centroids;

idx = zeros(m, 1);



for i = 1:max_iters

    fprintf('K-Means iteration %d/%d...', i, max_iters);

    if exist('OCTAVE_VERSION')

        fflush(stdout)

    end

    idx = findClosestCentroids(X, centroids);

    centroids = computeCentroids(X, idx, K);

end

end


A = double(imread('X.png'));

% Each RGB value ranges from 0-255 (8 bits representation).

% So, all values are in range 0-1

A = A/255;



img_size = size(A);

% Reshaping the img to have 1 pixel value in one row

X = reshape(A, img_size(1)*img_size(2), 3);



K = 16;  % No. of clusters required (#colors here)

max_iters = 10;



initial_centroids = kMeansInitCentroids(X, K);

% Run K-Means algo

[centroids, idx] = runkMeans(X, initial_centroids, max_iters);



idx = findClosestCentroids(X, centroids);

X_recovered = centroids(idx, :);

% Image represented by 3D matrix

X_recovered = reshape(X_recovered, img_size(1), img_size(2), 3);



% Display Original image

subplot(1, 2, 1);

imagesc(A);

title('Original');



% Display Compressed image

subplot(1, 2, 2);

imagesc(X_recovered);

title('Compressed image');
