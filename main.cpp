#include <iostream>
#include <opencv2/opencv.hpp>
#include <filesystem>
#include <fstream>

namespace fs = std::filesystem;

void resize_image(const std::string& image_path, const std::string& output_path, cv::Size target_size, int target_weight, bool remove_original) {
    cv::Mat img = cv::imread(image_path);
    
    if (img.empty()) {
        std::cout << "Could not read the image: " << image_path << std::endl;
        return;
    }
    
    std::ifstream file(image_path, std::ios::binary | std::ios::ate);
    std::streamsize original_weight = file.tellg();
    
    if (target_size.width != 0 && target_size.height != 0) {
        cv::resize(img, img, target_size);
    }
    
    if (target_weight != 0) {
        float scale_factor = std::sqrt(static_cast<float>(target_weight) / static_cast<float>(original_weight));
        cv::resize(img, img, cv::Size(), scale_factor, scale_factor);
    }
    
    cv::imwrite(output_path, img);
    
    if (remove_original) {
        fs::remove(image_path);
    }
}

void explore_directory(const std::string& directory, bool recursive, cv::Size target_size, int target_weight, bool remove_original) {
    for (const auto& entry : fs::directory_iterator(directory)) {
        if (entry.is_regular_file()) {
            std::string image_path = entry.path().string();
            std::string extension = entry.path().extension().string();
            std::transform(extension.begin(), extension.end(), extension.begin(), ::tolower);
            
            if (extension == ".png" || extension == ".jpg" || extension == ".jpeg") {
                std::string output_path = entry.path().parent_path().string() + "/resized_" + entry.path().filename().string();
                resize_image(image_path, output_path, target_size, target_weight, remove_original);
            }
        }
        else if (entry.is_directory() && recursive) {
            explore_directory(entry.path().string(), recursive, target_size, target_weight, remove_original);
        }
    }
}

int main(int argc, char** argv) {
    // TODO: Add argument parsing here
    
    std::string directory = "./my_images"; // Replace with argument
    bool recursive = false; // Replace with argument
    cv::Size target_size(300, 300); // Replace with argument
    int target_weight = 20000; // Replace with argument
    bool remove_original = false; // Replace with argument
    
    explore_directory(directory, recursive, target_size, target_weight, remove_original);
    
    return 0;
}

// g++ your_file.cpp -o output_name `pkg-config --cflags --libs opencv4`
